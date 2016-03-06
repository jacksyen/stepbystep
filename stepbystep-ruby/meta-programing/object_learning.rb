class ObjectLearning

  def p_object
    puts "Class's supperclass",Class.superclass
    puts "Module's supperclass:",Module.superclass
    puts "Objects's supperclass:",Object.superclass
    puts "BasicObject's SupperClass:",BasicObject.superclass
  end

end

object_learning =ObjectLearning.new
puts object_learning.class
object_learning.p_object

puts "string".class
puts String.class


