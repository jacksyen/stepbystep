ten_things = "Apples Oranges Crows Telephone Light Sugar"

puts "Wait there's not 10 things in that list, let's fix that."

stuff =ten_things.split(' ')
more_stuff =%w(Day Night Song Frisbee Corn Banana Girl Boy)


while stuff.length!=10
  next_one =more_stuff.pop
  puts "Adding: #{next_one}"
  stuff.push(next_one)
  puts "There is #{stuff.length} items now"
end

puts "There we go: #{stuff}"
puts "lets do some things with stuff"

puts stuff[1]
puts stuff[0]
puts stuff[-1] # the last one
puts stuff[11].nil? # nil
puts stuff.join(",")
puts stuff.pop()
puts stuff.push()
puts stuff.values_at(3,5).join("**")

