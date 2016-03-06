class MyClass
  puts 'hello'
end

result=class MyClass
  self
end

result

require_relative '../test/assertions'
assert_equal MyClass, result