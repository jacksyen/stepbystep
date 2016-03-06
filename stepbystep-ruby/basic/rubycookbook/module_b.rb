module A::B
  def doit
    puts "In Module A::B"
  end
  module_function :doit
end
