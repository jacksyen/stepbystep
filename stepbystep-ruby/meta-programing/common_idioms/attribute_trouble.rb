class MyClass
  attr_accessor :my_attribute

  def set_attribute(n)
    my_attribute = n
  end
end

obj = MyClass.new
obj.set_attribute 10
obj.my_attribute          # => nil

require_relative '../assertion.rb'
assert_equals nil, obj.my_attribute

class MyClass
  def set_attribute(n)
    self.my_attribute = n
  end
end

obj.set_attribute 10
obj.my_attribute          # => 10

assert_equals 10, obj.my_attribute

class MyClass
  private :my_attribute
end

obj.set_attribute 11      # No error!
obj.send :my_attribute    # => 11

assert_equals 11, obj.send(:my_attribute)

