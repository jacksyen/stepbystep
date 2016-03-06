"hello".class   # => String
String.class    # => Class

require_relative '../assertion.rb'

assert_equals String, "hello".class
assert_equals Class, String.class

# The "false" argument here means: ignore inherited methods
Class.instance_methods(false)   # => [:allocate, :new, :superclass]

assert_equals [:allocate, :new, :superclass], Class.instance_methods(false)

Array.superclass        # => Object
Object.superclass       # => BasicObject
BasicObject.superclass  # => nil

assert_equals Object, Array.superclass
assert_equals BasicObject, Object.superclass
assert_equals nil, BasicObject.superclass

Class.superclass        # => Module

assert_equals Module, Class.superclass


class MyClass; end
obj1 = MyClass.new
obj2 = MyClass.new

obj1.class          # => MyClass
obj2.class          # => MyClass

MyClass.superclass  # => Object
MyClass.class       # => Class

Class.superclass    # => Module
Module.superclass   # => Object

assert_equals MyClass, obj1.class
assert_equals MyClass, obj2.class
assert_equals Object, MyClass.superclass
assert_equals Class, MyClass.class
assert_equals Module, Class.superclass
assert_equals Object, Module.superclass


class MyClass
  def my_method; 'my_method()'; end
end

class MySubclass < MyClass
end

obj = MySubclass.new
obj.my_method()       # => "my_method()"

MySubclass.ancestors # => [MySubclass, MyClass, Object, Kernel, BasicObject]

assert_equals [MySubclass, MyClass, Object, Kernel, BasicObject], MySubclass.ancestors


class MyClass
  def my_method
    @v = 1
  end
end

obj = MyClass.new
obj.class           # => MyClass

obj.my_method
obj.instance_variables  # => [:@v]

assert_equals [:@v], obj.instance_variables

obj.methods.grep(/my/)  # => [:my_method]

assert_equals [:my_method], obj.methods.grep(/my/)

String.instance_methods == "abc".methods    # => true
String.methods == "abc".methods             # => false

assert_equals "abc".methods, String.instance_methods
assert_false "abc".methods == String.methods


class C
  def public_method
    self.private_method
  end

  private

  def private_method; end
end

C.new.public_method

class MyClass
  def my_method
    "original my_method()"
  end

  def another_method
    my_method
  end
end

module MyClassRefinement
  refine MyClass do
    def my_method
      "refined my_method()"
    end
  end
end

using MyClassRefinement
MyClass.new.my_method       # =>  "refined my_method()"
MyClass.new.another_method  # =>  "original my_method()"

assert_equals "refined my_method()", MyClass.new.my_method
assert_equals "original my_method()", MyClass.new.another_method


class MyClass
  def testing_self
    @var = 10     # An instance variable of self
    my_method()   # Same as self.my_method()
    self
  end

  def my_method
    @var = @var + 1
  end
end

obj = MyClass.new
obj.testing_self  # => #<MyClass:0x007f93ab08a728 @var=11>

