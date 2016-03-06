require_relative 'dsl.rb'

module Kernel
  def describe(description,&block)
    tests = Dsl.new.parse(description,block)
    tests.execute
  end
end

class Object
  def should
    self
  end
end