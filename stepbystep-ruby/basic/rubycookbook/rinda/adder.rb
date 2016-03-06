require_relative 'service'

class Adder < Service
  def process
    req = @ts.take([nil,nil,:+,Integer,Integer])
    p req
    respond(req,req[3]+req[4])
  end
end

Adder.new.run