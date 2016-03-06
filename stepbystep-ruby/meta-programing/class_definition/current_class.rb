class MyClass
  def my_method

  end
end

class MyClass
  def method_one
    def method_two
      'Hello'
    end
  end
end

obj=MyClass.new
# must invoke for invoking method_two
obj.method_one
obj.method_two

require_relative '../test/assertions'
assert_equal 'Hello',obj.method_two