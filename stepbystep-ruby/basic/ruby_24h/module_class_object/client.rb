require '../module_class_object/MyModule'
require '../module_class_object/Song'

puts MyModule::TARGET_FILE

MyModule.think

happy_bday = Song.new(["Happy birthday to you",
                       "I don't want to get sued",
                       "So I'll stop right there"])

happy_bday.sing_me_a_song