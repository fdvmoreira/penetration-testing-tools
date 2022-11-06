#!/usr/bin/python3

"""
Subdir_Enum: Enumerate subdirectories of a website

Author: Flavio Moreira

"""

import argparse
import requests

parser = argparse.ArgumentParser(prog="SubdirEnum", description="Enumerate subdirectories", epilog="Best regards,\nFlavio Moreira")
parser.add_argument("--url","-u","--ip", required=True, type=str, help="Url or IP address")
parser.add_argument("--wordlist", "-w", required=True, type=str, help="Wordlist file")
parser.add_argument("--protocol", "--proto", type=str, help="Protocol to use when IP address is provided")
parser.add_argument("--port", "-p", nargs="*", type=list, default=[80], help="Every port to enumerate the subdirectories")

# represents a subdirectory
class Subdirectory:
    pass

subdirectory = Subdirectory()

args = parser.parse_args(namespace=subdirectory)

for subdir in subdirectory.port:
    print(f"Fetching... port {subdir}")










