# ==============
# Objects
# all values are objects, and
# primitives types and object types is same
# ==============

# ==============
# class
# ==============
class Foo

end

# ==========
# initialize
# ==========
class Person
  def initialize(name)
    @name =name
  end
end

p = Person.new("patrick")

# =============
# getters and setters
# ==============
class Person
  def eyes
    @eyes
  end

  def eyes=(color)
    @eyes=color
  end
end

p1 = Person.new("simon")
p1.eyes ="patrick"
puts p1.eyes
# or

class Person
  attr_accessor :eyes
  def initialize(name)
    @eyes=name
  end
end

p2=Person.new("test")
puts p2.eyes