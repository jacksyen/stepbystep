require 'open-uri' # require for a module

open("http://www.baidu.com/") do |f|
  f.each_line {|line| p line}
  puts f.base_uri         # <URI::HTTP:0x40e6ef2 URL:http://www.ruby-lang.org/en/>
  puts f.content_type     # "text/html"
  puts f.charset          # "iso-8859-1"
  puts f.content_encoding # []
  puts f.last_modified    # Thu Dec 05 02:45:02 UTC 2002
end

#require and include difference
open("http://www.google.com") do |f|
	f.each_line {|line| p line}
	puts f.base_uri
	puts f.content_type
	puts f.charset
	puts f.content_encoding
end

# test rubymine for autocomplete
open("http://www.baidu.com") do |f|
  f.each { |line| puts line }
end
