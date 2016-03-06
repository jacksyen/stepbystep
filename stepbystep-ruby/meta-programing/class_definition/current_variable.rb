class C
  @@v =1
end

class D <C
  def my_method
    @@v
  end
end

D.new.my_method

require_relative '../test/assertions'
assert_equal 1,D.new.my_method

@@v=1

class MyClass
  @@v=2
end

@@v

assert_equal 2,@@v
