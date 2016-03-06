class C
  def initialize
    @x=1
  end
end

class D
  def twisted_method
    @y=2
    C.new.instance_eval{"@x:#{@x},@y:#{@y}"}
  end
end

D.new.twisted_method

class D
  def twisted_method
    @y=2
    C.new.instance_eval(@y){|y| "@x:#{@x},@y:#{y}"}
  end
end

p D.new.twisted_method