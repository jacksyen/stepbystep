require 'abbrev'
require 'readline'
include Readline

ABBREV = %w{exit inc dev}.abbrev
Readline.completion_proc = -> string {ABBREV[string]}

value = 0
loop do
  cmd = readline(" test [#{value}]",true) || "exit"
  case cmd.strip
    when "exit" then break
    when "inc"  then value +=1
    when "dec"  then value -=1
    else             puts "invalid command #{cmd}"
  end
end