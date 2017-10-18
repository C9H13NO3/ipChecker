# IP Checker
Forked from https://github.com/C9H13NO3/ipChecker
## About

I make use of an external service that alerts once a week on current open ports, compares those against previous results and updates accordingly. Said service does not make use of DNS and will only scan IP addresses.

My external IP is not static, and as such there is potential that it could change, resulting in the service I use scanning the wrong external IP. As such I wrote this script to check for any changes to my externally facing IP address, and email me if there has been one. 

## Use

Configure the config.py with details of your Gmail account, this will be used as the SMTP server. The currentIP address chan stay the same as on first run the script will update this with the latest. 

To use I set a cron job to run daily, it will take the currentIP and compare it against the output for the newIP, if there has been a change it will notify and update the config.py file with the now currentIP. 


