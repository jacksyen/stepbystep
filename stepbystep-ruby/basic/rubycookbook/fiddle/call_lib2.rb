require 'fiddle'
include Fiddle

lib = Fiddle.dlopen("lib.so")
print_msg = Fiddle::Function.new(lib['print_msg'],
[TYTP_VOIDP,TYPE_INT],
TYPE_INT)

msg_size = print_msg.call("Answer",42)
puts "Just wrote #{msg_size} bytes"