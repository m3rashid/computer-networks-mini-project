import socket
import threading
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9000

skt.bind((host, port))

aliases = []
clients = []
print('Listening for connections...')
skt.listen()

def broadcast(message):
  for client in clients:
    client.send(message)

def handle_client(client) :
  while True :
    try :
      str = input('Input the message to be broadcasted to the clients from the reciever -->\n').encode('utf-8')
      broadcast(str)
    except :
      index = clients.index(client)
      clients.remove(client)
      client.close()
      al = aliases[index]
      aliases.remove(al)
      print(f'{al} has left the chatroom')
      break
      

def recieve () :
  while True :
    client, address = skt.accept()
    print(f'connection is established with {str(address)}')
    client.send('alias?'.encode('utf-8'))
    alias = client.recv(1024)
    al = alias.decode('utf-8')
    aliases.append(al)
    clients.append(client)
    print(f'The alias of this client is --> {al}')
    broadcast(f'{al} has connected to the chat room'.encode('utf-8'))
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
  
  
if __name__ == '__main__' :
  recieve()