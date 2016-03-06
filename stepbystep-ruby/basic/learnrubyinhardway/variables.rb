cars =10
space_in_a_car =4.0
drivers = 30
is_boolean = true

puts "There are #{cars} cars available"
puts "There are only #{drivers} drivers available"

puts "There are #{space_in_a_car} spaces available"
puts "total space #{space_in_a_car*drivers}"
puts "boolean value #{is_boolean}"

test_string = "#{space_in_a_car}"
# todo to_s
puts test_string + drivers.to_s

while line =gets
  printf "%d:%10s[%d] %s",ARGF.lineno,ARGF.filename,ARGF.file.lineno,line
end