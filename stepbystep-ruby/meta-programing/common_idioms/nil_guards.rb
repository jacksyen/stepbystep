a ||= []

a || (a = [])

if defined?(a) && a
  a
else
  a = []
end

class C
  def initialize
    @a = []
  end

  def elements
    @a
  end
end

class C
  def elements
    @a ||= []
  end
end

def calculate_initial_value
  puts 'called: calculate_initial_value'
  false
end

b = nil
2.times do
  b ||= calculate_initial_value
end

if defined?(b) && b
  # if b is already defined and neither nil nor false:
  b
else
  # if b is undefined, nil or false:
  b = calculate_initial_value
end
