require 'abbrev'

COMMANDS = %w{sample send start status stop}.abbrev

while line = gets
  line = line.chomp
end

case COMMANDS[line]
  when "sample" then
    puts "sample"
  when "send" then puts "send"
  else
    STDERR.puts("Unknown command: #{line}")
end


