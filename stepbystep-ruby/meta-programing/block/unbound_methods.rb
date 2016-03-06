
module MyModule
  def my_method
    42
  end
end

unbound = MyModule.instance_method(:my_method)
unbound.class

p unbound
p local_variables

String.send :define_method,:another_method,unbound

p "abc".another_method

