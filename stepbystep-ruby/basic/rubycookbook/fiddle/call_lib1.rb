require 'dl/import'

module Message
  extend DL::Importer
  dlload "lib.so"
  extern "int print_msg(char *,int)"
end

msg_size = Message.print_msg("Answer",42)
puts "Just wrote #{msg_size} bytes"