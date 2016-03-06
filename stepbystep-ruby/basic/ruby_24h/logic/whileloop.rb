i=0
numbers =[]

while i<6
  puts "At the top is #{i}"
  numbers.push(i)
  i=i+1
  puts "Numbers now: #{numbers}"
  puts "at the bottom i is #{i}"

end

puts "the numbers: #{numbers}"

for i in numbers
  puts i
end