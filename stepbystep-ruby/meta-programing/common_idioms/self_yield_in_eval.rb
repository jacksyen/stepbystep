String.class_eval do |klass|
  klass # => String
end

require_relative '../assertion.rb'
assert_equals String, String.class_eval {|klass| klass }
