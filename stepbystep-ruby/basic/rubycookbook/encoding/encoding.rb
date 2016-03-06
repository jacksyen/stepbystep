require_relative('iso_8859_1')
require_relative('utf')

def show_encoding(str)
  puts "#{str}, #{str.bytes.to_a},#{str.encoding.name},#{str.bytesize}"
end

show_encoding(STRING_ISO)
show_encoding(UTF)
show_encoding('cat')
