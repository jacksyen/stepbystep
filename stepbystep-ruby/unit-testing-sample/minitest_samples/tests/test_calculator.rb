require 'minitest/autorun'
require_relative '../lib/calculator.rb'

class TestCalculator < Minitest::Test
  def setup
    @calculator = Calculator.new
  end

  def test_add
    assert_equal 4,@calculator.add(1,3)
  end

  def test_substract
    assert_equal 1,@calculator.subtract(3,2)
  end
end