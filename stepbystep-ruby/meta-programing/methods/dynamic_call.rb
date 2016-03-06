class MyClass
  def my_method(my_arg)
    my_arg * 2
  end

  define_method :my_method_3 do |my_arg|
    my_arg * 3
  end
end

obj = MyClass.new
p obj.my_method(3)  # => 6

p obj.send(:my_method, 3)   # => 6
p obj.my_method_3(4)