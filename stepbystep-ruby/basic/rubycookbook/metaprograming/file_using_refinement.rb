require_relative 'vanity1'
using VanityPuts

puts "I'm in #{File::basename(__FILE__)}"

def shout(msg)
  puts(msg.upcase)
end

shout("hello world")