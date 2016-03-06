require 'minitest/autorun'

def replace(array, original, replacement)
  array.map { |e| e == original ? replacement : e }
end

class ReplacementTest < Minitest::Test
  def test_replace
    original = %w(one two one three)
    replaced = replace(original, 'one', 'zero')
    assert_equal %w(zero two zero three), replaced
  end
end

class Array
  def replace(original, replacement)
    self.map { |e| e == original ? replacement : e }
  end
end


class ArrayExtensionTest < Minitest::Test
  def test_replace
    original = %w(one two one three)
    replaced = original.replace('one', 'zero')
    assert_equal %w(zero two zero three), replaced
  end
end
