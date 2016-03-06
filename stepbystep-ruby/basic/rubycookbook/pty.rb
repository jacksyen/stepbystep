require 'pty'
require 'expect'

$expect_verbose =true

PTY.spawn("irb") do |reader,writer,pid|
  reader.expect(/> /)
  writer.puts "'cat'.upcase"
  reader.expect("=> ")
  answer = reader.gets
  puts "Answer = #{answer}"
end