c = Class.new(Array) do
  def my_method
    'Hello'
  end
end

MyClass = c
c.name

require_relative '../test/assertions'

assert_equal MyClass,c
assert_equal 'MyClass',c.name