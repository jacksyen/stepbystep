require 'irb'

trap "INT" do
  IRB.start
end

count = 0
loop do
  count +=1
  puts count
  puts "Value = #{@value}" if defined? @value
  sleep 1
end