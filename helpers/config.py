'''

    Pentest Help Config File Handler

'''
import os
import json

config_file_path = os.getcwd() + "/pt-help.json"

class Config:
    def __init__(self):
        self.RHOST = '127.0.0.1'
        self.LHOST = '127.0.0.1'
        self.LPORT = '4444'
    
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

    def update_attr(self, attr, value):
        setattr(self, attr, value)
        self.update_config()

    def update_config(self):
        dictionary = self.__dict__ 
        # Serializing json  
        json_object = json.dumps(dictionary, indent = 4) 
        
        # Writing to file    
        with open(config_file_path, "w") as outfile: 
            outfile.write(json_object)

def check_config_file():    
    return os.path.exists(config_file_path)

def create_config_file():
    print("[+] Creating a default config file.")
    config = Config()
    dictionary = config.__dict__ 
    # Serializing json  
    json_object = json.dumps(dictionary, indent = 4) 
    
    # Writing to file    
    with open(config_file_path, "w") as outfile: 
        outfile.write(json_object) 

def read_config():
    with open(config_file_path, 'r') as openfile: 
        json_object = json.load(openfile)     
    return Config(json_object)
