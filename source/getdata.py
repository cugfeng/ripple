#!/usr/bin/python

import websocket
import time
import json
import os
import logging
from optparse import OptionParser

server="wss://s1.ripple.com"
buy_offer_cmd='{ \
	"command":"subscribe", \
	"id":"buy", \
	"books":[{ \
		"snapshot":true,  \
		"taker_gets":{ \
			"currency":"CNY", \
			"issuer":"rnuF96W4SZoCJmbHYBFoJZpR8eCaxNvekK" \
		}, \
		"taker_pays":{ \
			"currency":"XRP" \
		} \
	}] \
}'
sell_offer_cmd='{ \
	"command":"subscribe", \
	"id":"sell", \
	"books":[{ \
		"snapshot":true,  \
		"taker_gets":{ \
			"currency":"XRP" \
		}, \
		"taker_pays":{ \
			"currency":"CNY", \
			"issuer":"rnuF96W4SZoCJmbHYBFoJZpR8eCaxNvekK" \
		} \
	}] \
}'
offer_dict = {}
last_output_file = {}

def output_data(time, id, rate):
	global last_output_file

	file_name = os.path.join("data", time.split()[0])
	if "name" not in last_output_file:
		last_output_file["name"]    = file_name
		last_output_file["object"]  = open(file_name, "a")
		last_output_file["counter"] = 0
	elif file_name != last_output_file["name"]:
		last_output_file["object"].flush()
		last_output_file["object"].close()
		last_output_file["name"]    = file_name
		last_output_file["object"]  = open(file_name, "a")
		last_output_file["counter"] = 0

	last_output_file["object"].write("%s,%s,%0.04f\n" % (time, id, rate))
	last_output_file["counter"] += 1
	if last_output_file["counter"] > 7:
		last_output_file["object"].flush()
		last_output_file["counter"] = 0

# TODO: should not name variable as 'id'
def get_offer(offer, id):
	logging.debug(">>>get_offer %s" % id)
	logging.debug(offer)

	if id:
		gets = float(offer["TakerGets"]["value"])
		pays = float(offer["TakerPays"]) / 1000000
		rate = gets / pays
	else:
		gets = float(offer["TakerGets"]) / 1000000
		pays = float(offer["TakerPays"]["value"])
		rate = pays / gets

	return (id, gets, pays, rate)

def parse_offers(offers, id):
	logging.debug(offers)

	if id == "buy":
		# Buy offer
		for offer in offers:
			currency = offer["TakerGets"]["currency"] 
			if currency == "CNY":
				key   = offer["Account"] + "_" + str(offer["Sequence"])
				value = get_offer(offer, True)
				offer_dict[key] = value
				logging.info("Buy offer: %.01f XRP @ %.04f" % (value[1], value[3]))
	elif id == "sell":
		# Sell offer
		for offer in offers:
			currency = offer["TakerPays"]["currency"] 
			if currency == "CNY":
				key   = offer["Account"] + "_" + str(offer["Sequence"])
				value = get_offer(offer, False)
				offer_dict[key] = value
				logging.info("Sell offer: %.01f XRP @ %.04f" % (value[2], value[3]))

def parse_modified_node(node, id):
	if node["LedgerEntryType"] != "Offer":
		return

	logging.debug(">>>parse_modified_node %s" % id)
	logging.debug(node)

	current_time=time.strftime("%Y-%m-%d %H:%M:%S")
	if id == "buy":
		fields_list = []
		previous_fields = node["PreviousFields"]
		currency = previous_fields["TakerPays"]["currency"]
		if currency == "CNY":
			offer = get_offer(previous_fields, False)
			fields_list.append(offer)
		final_fields = node["FinalFields"]
		currency = final_fields["TakerPays"]["currency"] 
		if currency == "CNY":
			offer = get_offer(final_fields, False)
			fields_list.append(offer)
		gets = fields_list[0][1] - fields_list[1][1]
		pays = fields_list[0][2] - fields_list[1][2]
		rate = fields_list[0][3]
		logging.info("[%s] Buy: %0.1f XRP @ %.04f" % (current_time, gets, rate))
	elif id == "sell":
		fields_list = []
		previous_fields = node["PreviousFields"]
		currency = previous_fields["TakerGets"]["currency"]
		if currency == "CNY":
			offer = get_offer(previous_fields, True)
			fields_list.append(offer)
		final_fields = node["FinalFields"]
		currency = final_fields["TakerGets"]["currency"] 
		if currency == "CNY":
			offer = get_offer(final_fields, True)
			fields_list.append(offer)
		gets = fields_list[0][1] - fields_list[1][1]
		pays = fields_list[0][2] - fields_list[1][2]
		rate = fields_list[0][3]
		logging.info("[%s] Sell: %0.1f XRP @ %.04f" % (current_time, gets, rate))
	output_data(current_time, id, rate)

def parse_created_node(node, id):
	if "NewFields" not in node:
		return
	if "LedgerEntryType" not in node:
		return
	if node["LedgerEntryType"] != "Offer":
		return

	logging.debug(">>>parse_created_node %s" % id)
	logging.debug(node)

	new_fields = node["NewFields"]
	current_time = time.strftime("%Y-%m-%d %H:%M:%S")
	if id == "buy":
		offer = get_offer(new_fields, True)
		logging.info("[%s] Buy offer: %0.1f XRP @ %.04f" % (current_time, offer[2], offer[3]))
	elif id == "sell":
		offer = get_offer(new_fields, False)
		logging.info("[%s] Sell offer: %0.1f XRP @ %.04f" % (current_time, offer[1], offer[3]))

def parse_transaction(data):
	logging.debug(">>>parse_transaction")
	logging.debug(data)
	transaction = data["transaction"]
	transaction_type = transaction["TransactionType"]
	if transaction_type == "OfferCancel":
		key = transaction["Account"] + "_" + str(transaction["OfferSequence"])
		#del offer_dict[key]
	elif transaction_type == "OfferCreate":
		id = "sell"
		if "value" in transaction["TakerGets"]:
			id = "buy"

		for affected_node in data["meta"]["AffectedNodes"]:
			logging.debug(">>>affected_node")
			logging.debug(affected_node)
			if "ModifiedNode" in affected_node:
				parse_modified_node(affected_node["ModifiedNode"], id)
			elif "CreatedNode" in affected_node:
				parse_created_node(affected_node["CreatedNode"], id)

def parse_result(web_socket, result):
	logging.debug(">>>parse_result")
	logging.debug(result)
	try:
		data=json.loads(result)
		if "id" in data:
			parse_offers(data["result"]["offers"], data["id"])
		elif data["engine_result"] == "tesSUCCESS":
			parse_transaction(data)
	except (ValueError, KeyError) as exception:
		logging.warning(exception)

def send_message(web_socket):
	logging.debug("Send buy/sell offer command")
	web_socket.send(buy_offer_cmd)
	web_socket.send(sell_offer_cmd)

def main_socket():
	web_socket = websocket.WebSocketApp(url=server)
	try:
		web_socket.on_open    = send_message
		web_socket.on_message = parse_result
		web_socket.run_forever(ping_interval=45)
		web_socket.close()
	except AttributeError as exception:
		logging.warning(exception)
		logging.error("Connection to Ripple server failed!")
		exit(-1)

def main_file():
	dir_logs = "logs"
	names = os.listdir(dir_logs)
	for name in names:
		if name.endswith(".result"):
			path = os.path.join(dir_logs, name)
			logging.debug("Feed %s" % path)
			file_log = open(path, "r")
			for line in file_log:
				parse_result(None, line)
			file_log.close()

def init_logging(verbose):
	if verbose:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option("-f", "--file",
			action="store_true", dest="feed_file", default=False,
			help="feed data by file instead of websocket")
	parser.add_option("-v", "--verbose",
			action="store_true", dest="verbose", default=False,
			help="show verbose information")
	(options, args) = parser.parse_args()
	init_logging(options.verbose)
	if options.feed_file:
		main_file()
	else:
		main_socket()

