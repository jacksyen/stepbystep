class C
  def my_attribute=(value)
    @p = value
  end

  def my_attribute
    @p
  end
end

obj = C.new
obj.my_attribute = 'some value'
obj.my_attribute    # => "some value"

require_relative '../assertion.rb'
assert_equals "some value", obj.my_attribute
