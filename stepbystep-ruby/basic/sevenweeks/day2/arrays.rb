animals=%w('cat', 'dog', 'bears')

animals.each { |animal|
  puts animal.to_s
}

# index of array
puts 'learning array index'
puts animals[0]
puts animals[1]
puts animals[-1]
puts animals[0..1]
puts animals[0..1].class

# symbol and string is different
puts [1].methods.include?(:[])
puts [1].methods.include?('[]')

# array operation
puts('learning array operation')
animals.push('sneak')

animals.pop()

puts(animals)