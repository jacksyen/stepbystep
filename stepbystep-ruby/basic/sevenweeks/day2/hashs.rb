numbers ={
    1=>'one',
    2=>'two'
}

puts numbers
puts numbers[1]

stuff ={
    :array=>[1,2,3,4],
    :string=> 'cat',
    :hash=>{'key'=> 'value', :key1=> 'value1'}
}

puts stuff

# symbol magic
puts 'learning symbol magic'
puts 'string'.object_id
puts 'string'.object_id
puts :string.object_id
puts :string.object_id

# parameter with hash
def tell_the_true(options={})
  if(options[:prof]==:lawyer)
    'lawyer is coming'
  else
    "be careful,don't talk too much"
  end
end

puts tell_the_true
puts tell_the_true :prof=>:lawyer
