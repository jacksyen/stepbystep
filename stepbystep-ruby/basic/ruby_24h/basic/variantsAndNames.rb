cars =100
space_in_car=4.0
passangers =90
drivers =30

cars_driven = drivers
carpool_capacity = cars_driven*space_in_car
average_passengers_per_car=passangers/cars_driven

puts "There is #{cars} cars available"
puts "There are only #{drivers} drivers available"
