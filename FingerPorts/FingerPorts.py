#!/usr/bin/env python3

import sys, nmap

def nmapScanner(nmapScan):

	nm = nmap.PortScanner()
	nm.scan(nmapScan)
	nm.command_line()
	nm.scaninfo()
	nm.all_hosts()
	
	for host in nm.all_hosts():
		print('----------------------------------------------------')
		print('Host : %s (%s)' % (host, nm[host].hostname()))	
		print('Status : %s' % nm[host].state())

	for proto in nm[host].all_protocols():
		print('----------')
		print('Protocolo : %s' % proto)

	lport = nm[host][proto].keys()
	for port in lport:
		print('porta : %s\tstatus : %s' % (port, nm[host][proto][port]['state']))


nmapScanner(nmapScan = sys.argv[1])