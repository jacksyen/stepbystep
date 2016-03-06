require 'drb'

class TestServer
  def add(*args)
    args.inject{|n,v| n+v}
  end
end

server = TestServer.new
DRb.start_service("druby://localhost:9000",server)
