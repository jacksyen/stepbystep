require_relative 'executor.rb'

class Dsl
  def initialize
    @tests={}
  end

  def parse(description,block)
    self.instance_eval(&block)
    Executor.new(description,@tests)
  end

  def it(description,&block)
    @tests[description] =block
  end
end

