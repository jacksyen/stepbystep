require 'highline'

hl = HighLine.new
friends = hl.ask("Friends?", lambda {|s| s.split(',') })
puts "You're friends with: #{friends.inspect}"

name = hl.ask("Name?", lambda {|s| s.capitalize })
puts "Hello, #{name}"
