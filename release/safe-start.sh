#!/bin/bash

success=false
while [ $success == false ]; do
	python getdata.py
	if [ $? -ne 0 ]; then
		sleep 60
	else
		success=true
	fi
done

