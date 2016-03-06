require 'expect'
require 'socket'

$expect_verbose =true

socket = TCPSocket.new("localhost","ftp")

socket.expect("ready")
socket.puts("user testuser")
socket.expect("331 user testuser accepted,provide password.")
socket.puts("pass wibble")
socket.expect("logged in . \r\n")
socket.puts("pwd")
puts(socket.gets)
socket.puts "quit"