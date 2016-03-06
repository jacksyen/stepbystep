require 'socket'
socket = UDPSocket.new
socket.bind("127.0.0.1",12121)

loop do 
  msg,sender = socket.recvfrom(100)
  host = sender[3]
  puts "#{Time.now}: #{host} '#{msg}'"
  STDOUT.flush
end