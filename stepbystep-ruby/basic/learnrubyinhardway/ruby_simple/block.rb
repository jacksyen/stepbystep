def call_block
  puts "start block"
  yield
  yield
  puts "end of block"
end

call_block{puts "block is being executed"}

def call_block_with_paramters
  yield("simon","patrick")
end

call_block_with_paramters {|first_name,last_name| puts "#{first_name},#{last_name}"}

