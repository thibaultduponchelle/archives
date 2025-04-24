# Echo server program
import socket
import sys
import thread

def broadcast_clients(data):
  ''' Envoyer a tous les clients (pas uniquement la socket courante) '''
  for s in lsc:
    s.sendall(data)

def server_thread(conn, addr):
  ''' This is what will be launched in parallel'''    
  print 'Connected by', addr
  while 1:
    data = conn.recv(1024)
    if data: 
      print data
      conn.sendall(data)
  conn.close()

   
if __name__ == "__main__":
  print "### BUBBLE CRUSHER SERVER IS RUNNING ###"
  
  HOST = ''                 
  PORT = 50007              
  if len(sys.argv) > 1:
    print "Use %s as port number" %(sys.argv[1])
    PORT = int(sys.argv[1])

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind((HOST, PORT))

  while 1:
    s.listen(1)
    conn, addr = s.accept()
    if conn:
      thread.start_new_thread(server_thread, (conn, addr))
      
   

