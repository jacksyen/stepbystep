my_var = 'Success'

MyClass = Class.new do
  puts "#{my_var} in class definition"
  class_var = 'class var'

  define_method :my_method do
    puts "#{class_var}"
    puts "#{my_var} in the method"
  end
end

## instance variable
## class variable
## global variable

MyClass.new.my_method