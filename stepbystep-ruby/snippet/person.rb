class Person
  attr_accessor :age
  def initialize(options)
    self.age=options[:age]
  end

  def teenager?
    (13..19)===age
  end
end

options = {:age=>15};
p = Person.new(options)
puts p.teenager?