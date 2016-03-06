# Self method

class Dave

  def self.say_hello
    puts 'Hi'
  end

  def say_hello
    puts 'Hi Dave'
  end
end

Dave.say_hello

d = Dave.new
d.say_hello

animal='Cat'

def animal.say_hello
  puts 'miao miao'
end

animal.say_hello