def words_from_string(string)
  string.downcase.scan(/[\w']+/)
end

puts words_from_string("test test1")