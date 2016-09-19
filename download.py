#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()
import simplejson as json
import optparse
import sys

form = cgi.FieldStorage()
data = form['filename'].file

location_database = open('/home/bioinformatics2/DW/taxo.json', 'r')
database = json.load(location_database)

print "Content-Disposition: attachment; filename=script.csv"
print ""
for line in data: 
 for taxonomy in database:	
  if taxonomy["genus"] == line.replace('\r\n','') :
   print "Kingdom: %s," % taxonomy['kingdom'],
   print "phylum: %s," % taxonomy['phylum'],
   print "class: %s," % taxonomy['class'],
   print "order: %s," % taxonomy['order'],
   print "family: %s," % taxonomy['family'],
   print "genus: %s" % taxonomy['genus']
   print "<br/>"
   break
 else:
   print "No found genus on taxanomy"
   print "<br/>"




	

  
