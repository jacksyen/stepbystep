require_relative 'trace_calls'

class Example
  def one(arg)
    puts "One called with #{arg}"
  end
end

ex1 =Example.new
ex1.one("Hello")

class Example
  include TraceCalls
  def two(arg1,arg2)
    arg1+arg2
  end
end

ex1.one("world")
puts ex1.two(4,5)