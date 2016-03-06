require 'date'

class Person
  def initialize(name,dob)
    @name=name
    @dob=Date.parse(dob)
  end

  def age
    Date.today.year-@dob.year
  end

  def marry(someone)
    return someone
  end
end

fred =Person.new('Fred','1980-12-6')
p fred

puts fred.age

