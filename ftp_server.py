import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 2:
	print('please enter IP address of FTP server')
	sys.exit()
 
HOST = sys.argv[1]
PORT = 12345
s.connect((HOST, PORT))


def exit():
	s.close()   


def list():
	s.send(b'LIST')


def upld(file_name):
	s.send(b'UPLD')
	s.send(file_name.encode())	
	with open(file_name , 'rb') as f:	
		l = f.read(1024)
		while l:
			s.send(l)
			l = f.read(1024)
			

def dwld(file_name):
	s.send(b'DWLD')
	s.send(file_name.encode())

	with open(file_name , 'wb') as f:
		while True:	
			data = s.recv(1024)
			if not data:
				break
			f.write(data)


def main():

	print("\n\nWelcome to the FTP client.\n\nCall one of the following functions:\nUPLD file name : Upload file\nLIST           : List files\nDWLD  file name: Download file\nEXIT           : Exit\n")
	while True:
		print('enter a command')
		inp = input()
	
		if inp[:4] == 'LIST':
			list()

		elif inp[:4] == 'EXIT':
			exit()
			break

		elif inp[:4] == 'UPLD':
			upld(inp[5:])

		elif inp[:4] == 'DWLD':	
			dwld(inp[5:])
		else:
			print('Command not recognised; please try again')

if __name__ == "__main__":
	main()
