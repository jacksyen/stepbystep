class Fixnum
  alias_method :old_plus, :+

  def +(value)
    self.old_plus(value).old_plus(1)
  end
end

require_relative '../test/assertions'
assert_equal 3, 1 + 1
assert_equal 1, -1 + 1
assert_equal 111, 100 + 10
