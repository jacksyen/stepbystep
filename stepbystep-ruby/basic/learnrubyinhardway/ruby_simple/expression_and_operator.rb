#====================
#operator
#====================
puts 1+2
puts 2*3
puts 1+2==3
puts 2**1024
puts "dog"+"pound"
puts "hi"*3  #hihihi

#=================
#if
#=================
if 2+2==5
  puts "true"
else
  puts "false"
end

#===============
#unless
#===============
puts :each
unless "5".respond_to?(:each)
  puts "do something"
else
  puts "do another"
end

puts "welcome!" unless ["jill","Bob","Allen"][rand(3)]=="Bob"

# ============
# Case
# ============
case rand(20)
  when 0..5
    puts "0-5"
  when 6..10
    puts "6-10"
  else
    puts "more than 10"
end