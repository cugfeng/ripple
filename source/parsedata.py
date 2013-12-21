#!/usr/bin/python

import os
import time
import string

js_dir   = "html/js"
data_dir = "data"

def write_to_js(js_path, data_list):
	js_object = open(js_path, "w")

	js_object.write("var chart_data = [\n")
	js_object.write("['Time', 'Buy', 'Sell'],\n")
	data_size = len(data_list)
	for i in range(0, data_size):
		data = data_list[i]
		js_object.write("['%s', %.04f, %.04f]" % data)
		if i < data_size - 1:
			js_object.write(",\n")
		else:
			js_object.write("\n")
	js_object.write("]\n")

	js_object.flush()
	js_object.close()

def parse_data(data_path, data_list):
	list_buy  = []
	list_sell = []
	last_time = None
	last_buy  = 0.0
	last_sell = 0.0

	data_object = open(data_path, "r")

	for line in data_object:
		line_data = line.split(",")
		if len(line_data) != 3:
			continue
		
		time_list    = line_data[0].split(":")
		current_time = string.join(time_list[:-1], ":")
		if last_time is not None and current_time != last_time:
			if len(list_buy) > 0:
				current_buy = float(sum(list_buy)) / len(list_buy)
				last_buy    = current_buy
				list_buy    = []
			else:
				current_buy = last_buy
			if len(list_sell) > 0:
				current_sell = float(sum(list_sell)) / len(list_sell)
				last_sell    = current_sell
				list_sell    = []
			else:
				current_sell = last_sell
			data_list.append((last_time, current_buy, current_sell))

		last_time = current_time
		if line_data[1] == "buy":
			list_buy.append(float(line_data[2]))
		elif line_data[1] == "sell":
			list_sell.append(float(line_data[2]))
	else:
		if len(list_buy) > 0:
			current_buy = float(sum(list_buy)) / len(list_buy)
		else:
			current_buy = last_buy
		if len(list_sell) > 0:
			current_sell = float(sum(list_sell)) / len(list_sell)
		else:
			current_sell = last_sell
		data_list.append((last_time, current_buy, current_sell))

	data_object.close()

if __name__ == "__main__":
	data_names = os.listdir(data_dir)
	for data_name in data_names:
		js_path  = os.path.join(js_dir, data_name + ".js")
		js_exist = os.access(js_path, os.R_OK)
		today    = time.strftime("%Y-%m-%d")
		if not js_exist or data_name == today:
			print "Parse %s" % data_name
			data_list = []
			data_path = os.path.join(data_dir, data_name)
			parse_data(data_path, data_list)
			write_to_js(js_path, data_list)
		else:
			print "Skip %s, already exist" % data_name
	os.system("./generate-html.sh")

