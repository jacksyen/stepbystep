require 'service'

class Expand < Service
  def process
    req=@ts.take([nil,nil,nil,Array,nill])
    p req
    request(*req[3]) do |response|
      p response
      req[3] =response.answer
      p req
      @ts.write(req)
    end
  end
end

Expand.new.run