import json
from time import sleep
import sys
import socket
import os
from _thread import *

config = {}
def reload_config():
    with open("conf.json", "r") as f:
        global config
        config = json.load(f)
    print("Reloaded Config!")

def dprint(msg, delay=0.03):
    for c in msg + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(delay)

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.130"
        self.port = 5000
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
n = Network()
reload_config()

commands = ["$reload"]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while 1:
    i = input("> ")
    if i[0] == config["commandPrefix"]:
        if i in commands:
            if i == commands[0]:
                n.send("[Logs] " + config["username"] + ": ran command " + i)
                reload_config()
        else:
            dprint("Unknown Command!", 0.05)
    else:
        n.send(config["username"] + ": " + i)