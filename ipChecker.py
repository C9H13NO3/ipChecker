#!/usr/bin/python

import os
import smtplib
from subprocess import PIPE, Popen
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import config as cfg

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

newIP = cmdline("curl -s checkip.dyndns.org | grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}'").strip()
currentIP = cfg.currentIP

if newIP != currentIP:
	fromaddr = cfg.fromaddr
	toaddr = cfg.toaddr
	emailpwd = cfg.emailpwd
	msg = MIMEMultipart()
	msg['From'] = "IP Checker"
	msg['To'] = toaddr
	msg['Subject'] = "IP Address Update"
 	
	body = "Your IP has changed, it is now: " + newIP
	msg.attach(MIMEText(body, 'plain'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, emailpwd)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	
	ipUpdate = 'sed -i s/currentIP.*/currentIP\ =\ \\"' + newIP + '\\"/g config.py'
	os.system(ipUpdate)
