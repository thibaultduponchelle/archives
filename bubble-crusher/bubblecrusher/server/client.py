# Echo client program
import socket
import sys
import thread

def client_thread():
  while 1:
    data = s.recv(1024)
    print 'Received', repr(data)

if __name__ == "__main__":
  print "### CLIENT ###"
  HOST = "127.0.0.1"    
  PORT = 50007              
  if len(sys.argv) > 1:
    print "Use %s as remote host" %(sys.argv[1])
    HOST = sys.argv[1]
  if len(sys.argv) > 2:
    print "Use %s as port number" %(sys.argv[2])
    PORT = int(sys.argv[2])
   
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))

  # On est bien connecte alors on lance un thread pour la reception des msg
  thread.start_new_thread(client_thread, ())

  # Ici on s'occupe de l'ecriture 
  print "Type your message"
  print "(exit = quit)"
  while 1:
    message = raw_input()
    if message == "quit": break
    s.sendall(message)
  s.close()
