#!/usr/bin/python

import os
import time
import string

js_dir   = "html/js"
data_dir = "data"

def parse_rate(data_path, data_list):
	list_buy  = []
	list_sell = []
	last_time = None
	last_buy  = 0.0
	last_sell = 0.0

	data_object = open(data_path, "r")

	for line in data_object:
		line_data = line.split(",")
		if len(line_data) != 4:
			continue
		
		current_time   = time.strptime(line_data[0], "%Y-%m-%d %H:%M:%S")
		current_minute = time.strftime("%H:%M", current_time)
		if last_time is not None:
			last_minute = time.strftime("%H:%M", last_time)
			if current_minute != last_minute:
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
				data_list.append((last_minute, current_buy, current_sell))

		last_time = current_time
		if line_data[1] == "buy":
			list_buy.append(float(line_data[3]))
		elif line_data[1] == "sell":
			list_sell.append(float(line_data[3]))
	else:
		if len(list_buy) > 0:
			current_buy = float(sum(list_buy)) / len(list_buy)
		else:
			current_buy = last_buy
		if len(list_sell) > 0:
			current_sell = float(sum(list_sell)) / len(list_sell)
		else:
			current_sell = last_sell
		last_minute = time.strftime("%H:%M", last_time)
		data_list.append((last_minute, current_buy, current_sell))

	data_object.close()

def write_rate(js_path, rate_list):
	js_object = open(js_path, "w")

	js_object.write("var rate_array = [\n")
	js_object.write("['Time', 'Buy', 'Sell'],\n")
	list_size = len(rate_list)
	for i in range(0, list_size):
		rate = rate_list[i]
		js_object.write("['%s', %.04f, %.04f]" % rate)
		if i < list_size - 1:
			js_object.write(",\n")
		else:
			js_object.write("\n")
	js_object.write("]\n")

	js_object.flush()
	js_object.close()

def parse_volume(data_path, volume_list):
	volume    = {"buy": 0.0, "sell": 0.0}
	last_time = None

	data_object = open(data_path, "r")

	for line in data_object:
		line_data = line.split(",")
		if len(line_data) != 4:
			continue
		
		current_time = time.strptime(line_data[0], "%Y-%m-%d %H:%M:%S")
		current_hour = current_time.tm_hour
		if last_time is not None:
			last_hour = last_time.tm_hour
			if current_hour != last_hour:
				time_string = time.strftime("%H:00", last_time)
				volume_list.append((time_string, volume["buy"], volume["sell"]))
				volume = {"buy": 0.0, "sell": 0.0}

		last_time = current_time
		volume[line_data[1]] += float(line_data[2])
	else:
		time_string = time.strftime("%H:00", last_time)
		volume_list.append((time_string, volume["buy"], volume["sell"]))

	data_object.close()

def write_volume(js_path, volume_list):
	js_object = open(js_path, "a")

	js_object.write("var volume_array = [\n")
	js_object.write("['Time', 'Buy', 'Sell'],\n")
	list_size = len(volume_list)
	for i in range(0, list_size):
		volume = volume_list[i]
		js_object.write("['%s', %.01f, %.01f]" % volume)
		if i < list_size - 1:
			js_object.write(",\n")
		else:
			js_object.write("\n")
	js_object.write("]\n")

	js_object.flush()
	js_object.close()

if __name__ == "__main__":
	data_names = os.listdir(data_dir)
	for data_name in data_names:
		js_path  = os.path.join(js_dir, data_name + ".js")
		js_exist = os.access(js_path, os.R_OK)
		today    = time.strftime("%Y-%m-%d")
		if not js_exist or data_name == today:
			print "Parse %s" % data_name
			data_path = os.path.join(data_dir, data_name)

			rate_list = []
			parse_rate(data_path, rate_list)
			write_rate(js_path, rate_list)

			volume_list = []
			parse_volume(data_path, volume_list)
			write_volume(js_path, volume_list)
		else:
			print "Skip %s, already exist" % data_name
	os.system("./generate-html.sh")

