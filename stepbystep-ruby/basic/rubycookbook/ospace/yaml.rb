require 'yaml'

class Special
  def initialize(valuable,volatile,precious)
    @valuable = valuable
    @volatile =volatile
    @precious =precious
  end

  def encode_with(properties)
    properties['precious'] = @precious
    properties['valueable']=@valuable
  end
  def to_s
    "#@valuable #@volatile #@precious"
  end
end

puts Special.new("abc","test","ttd")