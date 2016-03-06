require 'drb'

DRb.start_service()
obj = DRbObject.new(nil,"druby://localhost:9000")

puts "Sum is #{obj.add(1,2,3)}"

