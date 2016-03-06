arr = [1,2,3]

fork do
  arr << 4
  puts arr  # changed arr
end

# not changed arr
puts arr

