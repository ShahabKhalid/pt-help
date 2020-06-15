#!/usr/bin/python3
import sys

from helpers import config
from helpers.rev_shells import rev_shells
print("Pentest Help By Shahab Khalid")

config_data = None
available_params = ['RHOST', 'LHOST', 'LPORT']

def print_config():
    print("[+] Reading config...")
    config_data = config.read_config()
    print("|-----------------------------")
    print(f"| RHOST: {config_data.RHOST}")    
    print(f"| LHOST: {config_data.LHOST}")    
    print(f"| LPORT: {config_data.LPORT}")    
    print("|-----------------------------")

# Checking for config file
if(not config.check_config_file()):
    print("[x] Config file not found.")
    config.create_config_file()    
else:
    config_data = config.read_config()

if len(sys.argv) > 1:
    if sys.argv[1].lower() == "config":
        print_config()
    elif sys.argv[1].lower() == "set":
        if len(sys.argv) < 4:
            print(f"USAGE: {sys.argv[0]} SET [PARAM] [VALUE]")
            print("Available Parameters: RHOST, LHOST, LPORT")
        else:
            if sys.argv[2].upper() not in available_params:
                print(f"USAGE: {sys.argv[0]} SET [PARAM] [VALUE]")
                print("Available Parameters: RHOST, LHOST, LPORT")
            else:
                config_data.update_attr(sys.argv[2].upper(),sys.argv[3])
                print_config()
    elif sys.argv[1].lower() == "rev-shell":
        config_data = config.read_config()
        rev_shells(config_data.LHOST, config_data.LPORT)