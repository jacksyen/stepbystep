count =0
words = File.open("/usr/share/dict/words")
word1 = File.read("/usr/share/dict/words")

while word = words.gets
  word=word.chomp!
  if word.length==12
    puts word
    count+=1
  end
end


count1 = word1.scan(/^..........\n/).size
puts "#{count} twelve-character words"
puts "#{count1} words"