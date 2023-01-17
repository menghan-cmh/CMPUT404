import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
	with conn:
		print("Connected by ", addr)
		while True:
			data = conn.recv(BYTES_TO_READ)
			if not data:
				break
			print(data)
			conn.sendall(b"hi " + data)

def starter_server():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))

		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.listen()

		conn, addr = s.accept()
		handle_connection(conn, addr)
		

def start_threaded_server():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))

		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.listen()

		while True:
			conn, addr = s.accept()
			thread = Thread(target=handle_connection, args=(conn, addr))
			thread.run()

# starter_server()
start_threaded_server()