require 'service'

class Driver < Service
  def make_request
    request(:*,[:+,2,3],[:+,4,5]) do
      puts "Answer is #{resp.answer}"
      exit
    end
  end
end

d= Driver.new
d.make_request
sleep
