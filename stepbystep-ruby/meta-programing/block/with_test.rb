require 'minitest/autorun'
require_relative 'with'

class TestWith < Minitest::Test
  class Resource
    def dispose
      @disposed = true
    end

    def disposed?
      @disposed
    end
  end
  def setup
    @resource = Resource.new
  end
  def test_disposes_of_resources
    r = @resource
    with(r) {}
    assert r.disposed?
  end

  def test_disposes_of_resources_in_case_of_exception
    r = @resource
    assert_raises(Exception) {
      with(r) {
        raise Exception
      }
    }
    assert r.disposed?
  end
end
