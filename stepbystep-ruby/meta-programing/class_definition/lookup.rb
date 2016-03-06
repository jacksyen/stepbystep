class C
  def a_method
    'C#a_method()'
  end
end

class D <C

end

obj = D.new
obj.a_method

require_relative '../assertion.rb'

assert_equals "C#a_method()",obj.a_method

class << obj
  def a_singleton_method
    'obj@a_singleton_method()'
  end
end

assert_equals "obj@a_singleton_method()",obj.a_singleton_method

assert_equals D,obj.singleton_class.superclass

puts C.singleton_class
puts D.singleton_class
puts D.singleton_class.superclass

