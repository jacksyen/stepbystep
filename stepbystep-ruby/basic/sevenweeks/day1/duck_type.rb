puts(4.class)
puts(4.0.class)

x=4+4.0
puts(x)
puts(x.class)

# error,string can't be added to sum up with Fixnum
def sum_up
  4.to_s+'four'
end

puts(sum_up)

a=['100','200',200]
puts a.class

# duck typing, to_i
a.each { |item|
  puts item.to_i
}

a.push(200)
puts a.size
puts a.to_s

a.pop(200)
# todo why array is empty???
puts a.to_s
puts a.size

# todo list
# Ruby API docs
# replace string
# Ruby Regular Express
# Ruby range


