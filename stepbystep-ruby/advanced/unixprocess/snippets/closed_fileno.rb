password = File.open('/etc/passwd')
puts password.fileno
password.close
puts password.fileno