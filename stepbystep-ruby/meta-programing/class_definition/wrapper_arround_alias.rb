class String
  alias_method :real_length, :length

  def length
    real_length > 5 ? 'long' : 'short'
  end
end

'War and Peace'.length      # => "long"
'War and Peace'.real_length # => 13

require_relative '../assertion.rb'
assert_equals 'long', 'War and Peace'.length
assert_equals 13, 'War and Peace'.real_length