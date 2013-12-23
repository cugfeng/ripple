#!/usr/bin/python

import os
import sys
sys.path.append('../source')
from parsedata import parse_data

if __name__ == "__main__":
	js_dir   = "../html/js"
	data_dir = "../data"

	data_names = os.listdir(data_dir)
	for data_name in data_names:
		js_path   = os.path.join(js_dir, data_name + ".js")
		js_exist  = os.access(js_path, os.R_OK)
		data_path = os.path.join(data_dir, data_name)
		if not js_exist:
			parse_data(data_path, js_path)
		else:
			js_mtime   = os.path.getmtime(js_path)
			data_mtime = os.path.getmtime(data_path)
			if js_mtime < data_mtime:
				parse_data(data_path, js_path)
			else:
				print "Skip %s, %s already exist" % (data_path, js_path)
	os.system("cd ../source; ./generate-html.sh")

