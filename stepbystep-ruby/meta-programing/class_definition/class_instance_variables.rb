class MyClass
  @my_var=1
end

class MyClass
  @my_var =1
  def self.read
    @my_var
  end

  def write
    @my_var=2
  end

  def read
    @my_var
  end
end

obj = MyClass.new
obj.read

require_relative '../test/assertions'
assert_equal nil, obj.read

obj.write
obj.read
MyClass.read
puts MyClass.instance_variables
assert_equal 2,obj.read
assert_equal 1,MyClass.read