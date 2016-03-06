#==================
# Intro Ruby
#==================

#==================
# Types
#==================
# String
"a string"

#Symbol
:name

#Fixnum
42

# Float
3.14

#True/False/Nil Class
true
false
nil

x="a String"
x=1
x=2.3
x=true
x=false
x=nil

#===============
# array
#===============
countries=["canada","brazil","spain"]

#===============
# hash
#===============
person ={:name=>"Brock Whitten",:location=>"West End"}
puts person[:name]
puts "hash value"
puts person['name'].nil?  #nil
puts "this is #{person[:name]} from #{person[:location]}"
#===============
# collection (array of hashes)
#===============
people =[
    {:name=>"Brock Whitten",:location=>"West End"},
    {:name=>"Brian Leroux",:location=>"Gastown"},
    {:name=>"Thurston",:location=>"NYC"}
]

#=============
#methods
#=============
# a simple method
def hello
  puts "hello world"
end

def hello(place)
  puts "hello #{place}"
end

def hello(place="world",*args)
  puts "hello #{place}"
end

#=============
#block
#=============
3.times do
  puts "hello"
end

#============
# iterator over an array
#============
countries.each do |country|
  puts "hello #{country}"
end

#iterator over hash
person.each do |key,value|
  puts "the value of #{key}=#{value}"
end

# another block
countries.each { |country|puts country.capitalize}

#=================
#range
#=================
cold_war=1945..1989
alphabet = "a".."z"
cold_war.include?(1980) #=>true
alphabet.each { |l|print l} #=>print alphabet sequence

puts "\n"
sam =" "
def sam.play(word)
  p "hello #{word}" # "hello world " in console,which p is different with puts
end
sam.play("world")


