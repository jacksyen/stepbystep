module ExplicitString
  def length
    super > 5 ? 'long' : 'short'
  end
end

String.class_eval do
  prepend ExplicitString
end

'War and Peace'.length      # => "long"

require_relative '../assertion.rb'
assert_equals 'long', 'War and Peace'.length
