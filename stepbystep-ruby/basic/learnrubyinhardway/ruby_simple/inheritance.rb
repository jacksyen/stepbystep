# ====================
# inheritance
#
# classes can sharing_behavior value and
# behavior form another class
# =====================

# =====================
# simple inheritance
# =====================
class Animal
  def move
    puts "moving ...."
  end
end

class Bird<Animal
  def fly
    puts "flying ......"
  end
end

roy = Bird.new
roy.move
roy.fly

# ==================
# more inheritance
# =================
class Runner
  def speed
    4.0
  end
end

class Sprinter < Runner
  def speed
    super()*2
  end
end

class Jogger < Runner
  def speed
    super()*0.75
  end
end

j = Jogger.new
puts "J,the jogger runs at #{j.speed} mph"

m = Sprinter.new
puts "m,the sprinter runs at #{m.speed} mph"