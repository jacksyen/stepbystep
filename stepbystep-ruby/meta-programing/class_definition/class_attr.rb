class MyClass
  attr_accessor :a
end

obj = MyClass.new
obj.a=2
obj.a

require_relative'../test/assertions'

assert_equal 2,obj.a

class MyClass

end

class Class
  attr_accessor :b
end

MyClass.b=42
MyClass.b

assert_equal(42,MyClass.b)

class MyClass
  class << self
    attr_accessor :c
  end
end

MyClass.c ='It works'
MyClass.c

assert_equal 'It works',MyClass.c

def MyClass.c=(value)
  @c=value
end

def MyClass.c
  @c
end
# obj = MyClass.new
# obj.instance_variable_set('@c', 'it not works')
 MyClass.c='It works!!'
assert_equal 'It works',MyClass.c
