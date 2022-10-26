import socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alias = input('Please enter the alias for this client >>> ')


host = '127.0.0.1'
port = 9000
skt.connect((host, port))
# skt.send(f'{alias} connected from this side'.encode('utf-8'))
while True :
	try:
		str = skt.recv(1024).decode('utf-8')
		if str == 'alias?':
			skt.send(alias.encode('utf-8'))
		else :
			print(f'Server : {str}')
	except:
		print('error recieving infomation from the server')
		skt.close()
		break

