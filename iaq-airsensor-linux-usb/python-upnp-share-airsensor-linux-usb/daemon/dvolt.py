#!/usr/bin/env python

import sys, os, time, atexit
from signal import SIGTERM

class Daemon:
    """
    A generic daemon class.
   
    Usage: subclass the Daemon class and override the run() method
    """
    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
	    self.stdin = stdin
	    self.stdout = stdout
	    self.stderr = stderr
	    self.pidfile = pidfile
   
    def daemonize(self):
	    """
	    do the UNIX double-fork magic, see Stevens' "Advanced
	    Programming in the UNIX Environment" for details (ISBN 0201563177)
	    http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
	    """
	    try:
		    pid = os.fork()
		    if pid > 0:
			    # exit first parent
			    sys.exit(0)
	    except OSError, e:
		    sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
		    sys.exit(1)
   
	    # decouple from parent environment
	    os.chdir("/")
	    os.setsid()
	    os.umask(0)
   
	    # do second fork
	    try:
		    pid = os.fork()
		    if pid > 0:
			    # exit from second parent
			    sys.exit(0)
	    except OSError, e:
		    sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
		    sys.exit(1)
   
	    # redirect standard file descriptors
	    sys.stdout.flush()
	    sys.stderr.flush()
	    si = file(self.stdin, 'r')
	    so = file(self.stdout, 'a+')
	    se = file(self.stderr, 'a+', 0)
	    os.dup2(si.fileno(), sys.stdin.fileno())
	    os.dup2(so.fileno(), sys.stdout.fileno())
	    os.dup2(se.fileno(), sys.stderr.fileno())
   
	    # write pidfile
	    atexit.register(self.delpid)
	    pid = str(os.getpid())
	    file(self.pidfile,'w+').write("%s\n" % pid)
   
    def delpid(self):
	    os.remove(self.pidfile)

    def start(self):
	    """
	    Start the daemon
	    """
	    # Check for a pidfile to see if the daemon already runs
	    try:
		    pf = file(self.pidfile,'r')
		    pid = int(pf.read().strip())
		    pf.close()
	    except IOError:
		    pid = None
   
	    if pid:
		    message = "pidfile %s already exist. Daemon already running?\n"
		    sys.stderr.write(message % self.pidfile)
		    sys.exit(1)
	   
	    # Start the daemon
	    self.daemonize()
	    self.run()

    def stop(self):
	    """
	    Stop the daemon
	    """
	    # Get the pid from the pidfile
	    try:
		    pf = file(self.pidfile,'r')
		    pid = int(pf.read().strip())
		    pf.close()
	    except IOError:
		    pid = None
   
	    if not pid:
		    message = "pidfile %s does not exist. Daemon not running?\n"
		    sys.stderr.write(message % self.pidfile)
		    return # not an error in a restart

	    # Try killing the daemon process       
	    try:
		    while 1:
			    os.kill(pid, SIGTERM)
			    time.sleep(0.1)
	    except OSError, err:
		    err = str(err)
		    if err.find("No such process") > 0:
			    if os.path.exists(self.pidfile):
				    os.remove(self.pidfile)
		    else:
			    print str(err)
			    sys.exit(1)

    def restart(self):
	    """
	    Restart the daemon
	    """
	    self.stop()
	    self.start()

    def run(self):
	    """
	    You should override this method when you subclass Daemon. It will be called after the process has been
	    daemonized by start() or restart().
	    """




import usb.core
import usb.util
import sys
import time
import signal, os

interface = 0

def write_to_file(val):
  file = open('/var/www/voc/values.txt', 'w+')
  file.write(str(val))
  file.close()
  
dev = usb.core.find(idVendor=0x03eb, idProduct=0x2013)
if(dev == None):
  print "-- No voltcraft co2 found !"
else:
  print "-- device found  : ", 
  print dev
  if dev.is_kernel_driver_active(interface) is True:
    print "-- but we need to detach kernel driver"
    dev.detach_kernel_driver(interface)

  try:
    dev.set_configuration()
    dev.set_interface_altsetting(interface = 0, alternate_setting = 0)
  except usb.core.USBError as e:
    print "Could not set configuration: %s" % str(e)

class daemonVolt(Daemon):
  def run(self):
	while(1):
	  time.sleep(1)
	  data = []
	  c = 104
	  try:
	    print "Ask values..."
	    if(c<103):
	      c = 102
	    c += 1
	    if(c>255):
	      c = 104
	    req = "@" + chr(c) + "*TR\x0A@@@@@@@@@@"
	    print req
	    dev.write(0x02, req)
	    time.sleep(10/1000)
	    print "Read values..."
	    data = dev.read(0x81, 0x10)
	    try:
	      val = int(data[2]) + (int(data[3]) << 8)
	      print "data : %d" % val
	      write_to_file(val)
	    except:
	      pass
	    time.sleep(10/1000)
	    data = dev.read(0x81, 0x10)
	  except:
	    print "except"

if __name__ == "__main__":
        daemon = daemonVolt('/tmp/dvolt.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
