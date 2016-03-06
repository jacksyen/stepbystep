today = Time.now
puts today
if today.saturday?
  puts "sleeping"
elsif today.sunday?
       puts "relax"
else
  puts "go to work now"
end