require 'minitest/autorun'
require_relative 'customer'

class TestCustomer < MiniTest::Unit::TestCase

  def test_append
    c= Customer.new("simon","patrick")
    f= File.open('tmpfile',"w") do |f|
      c.append_name_to_file(f)
    end

    f=File.open("tmpfile") do |f|
      assert_equal("simon patrick",f.gets)
    end
  ensure
    File.delete("tmpfile") if File.exist?("tmpfile")
  end

  def test_append_empty_fle
    c= Customer.new("simon","patrick")
    f=[]
    c.append_name_to_file(f)
    assert_equal(["simon", " ", "patrick"], f)
  end

  def test_append_quota
    c=Customer.new("simon","patrick")
    f=" "
    c.append_name_to_file(f)
    assert_equal(" simon patrick",f)
  end
end