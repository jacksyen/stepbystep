class Greeting
  def initialize(msg)
    @msg=msg
  end

  def welcome
    @msg
  end
end

my_greeting = Greeting.new('hello')
puts my_greeting.welcome


class Greeting
  def initialize(text)
    @text = text
  end

  def welcome
    @text
  end
end

my_object = Greeting.new("Hello")

my_object.class                             # => Greeting
my_object.class.instance_methods(false)     # => [:welcome]
my_object.instance_variables                # => [:@text]

require_relative '../assertion.rb'
assert_equals Greeting, my_object.class
assert_equals [:welcome], my_object.class.instance_methods(false)
assert_equals [:@text], my_object.instance_variables