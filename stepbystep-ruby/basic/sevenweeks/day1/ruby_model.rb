# everything is object
puts(4.class)
puts(4.methods)
puts('==================')
puts('4'.class)
puts('4'.methods)
x=4
puts (x <= 5)

# False and True use different class
puts(false.class)
puts(true.class)


if x==4
  puts 'x is 4'
end

x=4
unless x==4
  puts 'x is not 4'
else
  puts "x is #{x}"
end

# false or true
puts(true && false)
puts true || this_will_not_cause_an_error
# this will cause error
# puts false || this_will_not_cause_an_error
# no error
puts true | this_will_cause_an_error

puts true | false