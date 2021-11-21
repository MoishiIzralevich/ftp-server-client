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


def list_files():
	s.send(b'LIST')


def upload_file(file_name):
	s.send(b'upload')
	s.send(file_name.encode())	
	with open(file_name , 'rb') as f:	
		l = f.read(1024)
		while l:
			s.send(l)
			l = f.read(1024)
			

def download_file(file_name):
	s.send(b'download')
	s.send(file_name.encode())

	with open(file_name , 'wb') as f:
		while True:	
			data = s.recv(1024)
			if not data:
				break
			f.write(data)


def main():

	print("\n\nWelcome to the FTP client.\n\nCall one of the following functions:\nupload file name : Upload file\nlist           : List files\ndownload  file name: Download file\nEXIT           : Exit\n")
	while True:
		print('enter a command')
		inp = input()
	
		if inp[:4] == 'list':
			list_files()

		elif inp[:4] == 'EXIT':
			exit()
			break

		elif inp[:6] == 'upload':
			upload_file(inp[7:])

		elif inp[:8] == 'download':	
			download_file(inp[9:])
		else:
			print('Command not recognised; please try again')

if __name__ == "__main__":
	main()
