#!/usr/bin/python3

"""
Hash Cracker
Crack hashes with wordlists. Algorithms supperted: [md5, sha256]

by Flavio Moreira
"""

import argparse
import pyfiglet
import hashlib

# setup banner
banner = pyfiglet.figlet_format("Hash Cracker")
print(banner)

# arguments handling
parser = argparse.ArgumentParser(prog="Hash Cracker", description="Crack MD5 and sha256 hashes with a wordlist", epilog="by Flavio Moreira")
parser.add_argument("--wordlist", "-w", required=True, type=str, help="Wordlist to use for cracking the hash")
parser.add_argument("--hash", "--dump", "-d", type=str, help="Hash to be cracked")

#Hash Cracker
class Cracker:
    pass

cracker = Cracker()
parser.parse_args(namespace=cracker)

worldlist = cracker.wordlist
hash = cracker.hash

# prompt the user to enter the hash if it has not been provided
if not hash:
    hash = str(input("Hash: "))

print(f"{hash}")



