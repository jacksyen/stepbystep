require 'socket'

socket = TCPServer.open('0.0.0.0',8080)

[:INT,:QUIT].each do |signal|
  Signal.trap(signal){
    wpids.each {|wpid| Process.kill(signal,wpid)}
  }
end

wpids =[]

5.times{
  wpids << fork do
    loop {
      connection = socket.accept
      connection.puts "Hello Readers!"
      connection.close
    }
  end
}

Process.waitall