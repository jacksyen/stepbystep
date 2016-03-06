class Xs
  include Comparable
  attr_accessor :length
  def initialize(n)
    @length = n
  end

  def succ
    puts @length
    return Xs.new(@length+1)
  end

  def <=>(other)
    puts other.length
    @length = other.length
  end

  def inspect
    puts 'x'*@length
  end
end

xs = Xs.new(10)
xs2= xs.succ
puts xs2.length
xs.inspect
xs.<=>(xs2)
puts xs.length
puts xs2.length