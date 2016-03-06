class MyClass
  def my_method;'my_method()';end
  alias_method :m,:my_method
end

obj=MyClass.new
obj.my_method
obj.m

require_relative '../test/assertions'
assert_equal 'my_method()', obj.my_method
assert_equal 'my_method()', obj.m

class MyClass
  alias_method :m2, :m
end

obj.m2           # => "my_method()"

assert_equal "my_method()", obj.m2


