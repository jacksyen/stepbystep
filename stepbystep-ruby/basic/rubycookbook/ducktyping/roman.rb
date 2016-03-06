class Roman
  MAX_ROMAN=4999

  attr_reader :value
  protected :value

  def initialize(value)
    if value<=0||value>MAX_ROMAN
      fail "Roman value #{value} is execeed the definition of Roman, 0-#{MAX_ROMAN}"
    end
    @value=value
  end

  def coerce(other)
    if Integer===other
      [ other,@value ]
    else
      [ Float(other),Float(@value) ]
    end
  end
end