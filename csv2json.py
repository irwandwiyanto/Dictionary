#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()
import csv
import json
import sys

form = cgi.FieldStorage()
csvfile = form['filename'].file

if "print" in form:
	fieldnames = ("kingdom","phylum","class","order","family","genus")
	reader = csv.DictReader( csvfile, fieldnames)
	out = json.dumps( [ row for row in reader ] )
	print "content-type: text/html\n"
	print "%s" % (out,)
elif "download" in form:
	fieldnames = ("kingdom","phylum","class","order","family","genus")
	reader = csv.DictReader( csvfile, fieldnames)
	out = json.dumps( [ row for row in reader ] )	
	print "Content-Disposition: attachment; filename=script.json"
	print ""
	print "%s" % (out,)
else:
    print "Not choice option"
