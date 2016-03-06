str = "just a regular string"

def str.title?
  self.upcase == self
end

str.title?                      # => false
str.methods.grep(/title?/)      # => [:title?]
str.singleton_methods           # => [:title?]

require_relative '../assertion.rb'
assert_false str.title?
assert_equals [:title?], str.methods.grep(/title?/)
assert_equals [:title?], str.singleton_methods
