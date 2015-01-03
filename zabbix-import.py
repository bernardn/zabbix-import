#!/usr/bin/env python
"""
zabbix-import.py

Imports XML config files into Zabbix using Zabbix API

It creates or updates all configuration elements described in the source XML file.

Version: 0.2
Author: Bernard Nauwelaerts
Date: 20140611

"""
import sys
import optparse
from xml.dom.minidom import parse
import json
from pyzabbix import ZabbixAPI, ZabbixAPIException

def main():
	p = optparse.OptionParser()

	p.add_option('--user', '-u', default="Admin")
	p.add_option('--password', '-p', default="zabbix")
	p.add_option('--server', '-s', default="http://127.0.0.1/zabbix")
	p.add_option('--file', '-f', default="hosts.xml")
	options, arguments = p.parse_args()

	try:
		dom  = parse(options.file)
		xml = dom.toxml()
	except:
		print "An error occured while parsing XML file"
		sys.exit(-1)

	rules = json.loads("""
	{
		"groups": {
			"createMissing": true,
			"updateExisting": true
		},
		"hosts": {
			"createMissing": true,
			"updateExisting": true
		},
		"interfaces": {
			"createMissing": true,
			"updateExisting": true
		},
		"applications": {
			"createMissing": true,
			"updateExisting": true
		},
		"items": {
			"createMissing": true,
			"updateExisting": true
		},
		"templates": {
			"createMissing": true,
			"updateExisting": true
		},
		"triggers": {
			"createMissing": true,
			"updateExisting": true
		},
		"templateLinkage": {
			"createMissing": true,
			"updateExisting": true
		}
	}
	""");


	""" Loading Zabbix API """
	try:
		zbx = ZabbixAPI(options.server)
	
	except ZabbixAPIException, e:
		print e.args[0]
		sys.exit(-1)

	""" Loggin in to Zabbix API """
	try:
		zbx.login(options.user,options.password)
	
	except ZabbixAPIException, e:
		print e.args[0]
		sys.exit(-1)

	""" Importing configuration """
	try:
		if zbx.confimport('xml', xml, rules):
			print "Configuration successfully imported"
		else:
			print "Configuration wasn't successfully imported"
			sys.exit(-1)
	
	except ZabbixAPIException, e:
		print e.args[0]
		sys.exit(-1)


if __name__ == '__main__':
	main()