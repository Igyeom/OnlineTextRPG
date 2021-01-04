import socket
from _thread import *
import sys
from better_profanity import profanity
profanity.load_censor_words()
server = "192.168.0.130"
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.bind((server, port))
except socket.error as e:
  print(str(e))

s.listen(20)
print("Server Started.")

def threaded_client(conn):
  reply = ""
  conn.send(str.encode("Successfully Connected!"))
  while 1:
    try:
      data = conn.recv(2048)
      reply = data.decode("utf-8")

      if not data:
        print("Someone disconnected!")
        break
      else:
        print("[Chat]" + profanity.censor(reply))
        conn.sendall(str.encode(profanity.censor(reply)))
    except:
      break

while 1:
  conn, addr = s.accept()
  print("Connected to: ", addr)
  start_new_thread(threaded_client, (conn,))
