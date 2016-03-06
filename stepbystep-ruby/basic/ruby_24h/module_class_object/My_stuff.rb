class MyStuff
  attr_reader :target_file
  def initialize
    @target_file = "target file"
  end

  def think()
    puts @target_file
  end
end