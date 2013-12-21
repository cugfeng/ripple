#!/bin/bash

cd html
for js_file in js/*.js; do
	js_name=`basename $js_file`
	date=`echo $js_name | sed 's/\.js$//'`
	html_name=$date.html

	if [ ! -f $html_name ]; then
		echo "Generate $html_name"
		cp -f template/chart.html $html_name
		sed -i "s/date/$date/" $html_name
	fi
done

