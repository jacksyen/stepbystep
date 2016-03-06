require_relative 'describe.rb'

describe "some test" do
  it "should be true" do
    true.should == true
  end
  it "should show that an expression can be true" do
    (5 == 5).should == true
  end

  it "should be failing deliberately" do
    5.should == 6
  end
end