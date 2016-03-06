module MyModule
  def my_method
    'hello'
  end
end

obj = Object.new
obj.extend MyModule

class MyClass
  extend MyModule
end

class MyIncludeModule
  include MyModule
end

puts MyClass.my_method
puts obj.my_method
puts obj.singleton_methods

class MyClassIncludeSolution
  class << self
    include MyModule
  end
end

begin
  puts MyIncludeModule.my_method
rescue NoMethodError
end


puts MyClassIncludeSolution.my_method