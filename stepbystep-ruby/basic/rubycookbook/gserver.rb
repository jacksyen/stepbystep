require 'gserver'

class TimeServer <GServer
  def initialize
    super(2000)
    @count = 3
  end

  def serve(client)
    client.puts Time.now
    @count -=1
    stop if @count.zero?
  end

end
