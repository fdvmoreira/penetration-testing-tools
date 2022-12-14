#!/usr/bin/python3

"""
Subdomain Scanner

Params:
    -w/--wordlist   : File containing words to use as subdomain
    -d/--domain/ip  : Domain or IP address ex: example.com, 125.165.2.44 
    --protocol      : Protocol to use with the domain/IP. HTTP, HTTPS, DNS
    -p/--port       : Target port default 80 for http and 443 for https
    -l/--log        : File to save the results to a log file 

Usage:
    ex1: ./subdomain_scanner.py example.com
"""

import sys
import requests
import argparse
from datetime import datetime as date

# Construct a dict with the cli args
parser = argparse.ArgumentParser(prog="Subdomain Scanner", description="Find subdomains with a wordlist file.", epilog="Best regards,\nFlavio Moreira\nGitHub : https://github.com/fdvmoreira")
parser.add_argument("--domain","-d","-u","--ip", required=True, type=str, help="Domain or IP address, ex: example.com")
parser.add_argument("--wordlist","-w", required=True, type=str,help="File containing words separated by newlines")
parser.add_argument("--protocol", type=str, default="http", choices=["http","https","dns"], help="Protocol to use for the request. Default=http. Supports HTTP, HTTPS, DNS")
parser.add_argument("--port","-p", default=80, type=int, help="Port Number. Default=80")
parser.add_argument("--log", "-l",type=str, help="File to save the logs to. Default=None")

class Scanner:
    pass

scanner = Scanner()

args = parser.parse_args(namespace=scanner)

input_file = scanner.wordlist 
protocol = scanner.protocol
port     = scanner.port
log      = scanner.log
domain   = scanner.domain

#File Mode
READ    = "r"
WRITE   = "w"
APPEND  = "a"

# Read file content
wordlist = None 
with open(input_file, READ) as file:
    wordlist = file.read()
    wordlist = wordlist.splitlines()

# Make request to each word in the list
for subdomain in wordlist:
    URL = f"{protocol}://{subdomain}.{domain}:{port}"
    response = None
    
    try:
        print(f"Trying {URL} ...")
        response = requests.get(URL)

    except Exception as err:

        print("^^^^^^^^^^^^^^^Failed!^^^^^^^^^^^^")
        # write log to log_file
        if log:
            with open(log,APPEND) as log_file:
               log_file.write(f"{date.now()} {err}\n") 

    else:
        print(f"Status {response.status_code} SUCCESS")
