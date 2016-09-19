#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()
import json as simplejson
import optparse
import sys
import csv

form = cgi.FieldStorage()
taxo_parsed = form['filename'].file

# open a file for writing

taxo_data = open('/var/www/html/cgi/tmp.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(taxo_data)

if "print" in form:
	count = 0
	for taxo in taxo_parsed:
		if count == 0:
			header = taxo.keys()
			csvwriter.writerow(header)
			count += 1
		out = csvwriter.writerow(taxo.values())
		print "content-type: text/html\n"
		print "%s" % (out,)

