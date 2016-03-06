require 'strscan'

values =[]

while line = gets
  scanner = StringScanner.new(line.chomp)
  scanner.scan(/(get|set)\s+/) or fail("missing command")
  cmd = scanner[1]
  var_name = scanner.scan(/\w+/) or fail("Missing variable")

  puts cmd
  puts var_name
  puts var_name.inspect
  case cmd
    when "get"
      puts "#{var_name} => #{values[var_name]}"
    when "set"
      scanner.skip(/\s+=\s+/) or fail "missing '='"
      value = scanner.rest
      values[var_name] =value
    else
      fail cmd
  end
end