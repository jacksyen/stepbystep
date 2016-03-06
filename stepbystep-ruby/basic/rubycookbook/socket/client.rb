require 'socket'

log = UDPSocket.new
log.connect("127.0.0.1",1212)
log.print "Up and Running"
log.print "done"

