puts Process.getpgrp
puts Process.pid

fork {
  puts Process.getpgrp
  puts Process.pid
}
