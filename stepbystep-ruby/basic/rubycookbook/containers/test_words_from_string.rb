require 'minitest/autorun'
require_relative 'words_from_string'

class TestWordsFromString < MiniTest::Unit::TestCase
  def test_words_from_string
    assert_equal(["test","test2"],words_from_string("test test2"))
  end
end