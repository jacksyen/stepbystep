# rudy doc
#

module Fibonacci
  # Calculate the first _count_ fibonacci, starting
  #
  # :call-seq:
  #   Fibonacci.sequence(count) (count,&block)
  #   Fibonacci.sequence(count){|val| ...} -> nil

  def Fibonacci.sequence(count,&block)
    result,block = setup_optional_block(block)
    generate do |val|
      break if count <=0
      count -=1
      block[val]
    end
    result
  end

  def Fibonacci.upto(max,&block)
    result,block = setup_optional_block(block)
    generate do |val|
      break if val>max
      block[val]
    end
    result
  end

  private
  def Fibonacci.generate
    f1,f2=1,1
    loop do
      yield f1
      f1,f2=f2,f1+f2
    end
  end

  def Fibonacci.setup_optional_block(block)
    if block.nil?
      [ result = [],lambda {|val| result << val} ]
    else
      [nil,block]
    end
  end
end
