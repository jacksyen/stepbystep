3.times{
  puts 'learning block'
}


class Fixnum
  def my_times
    i=self
    while i>0
      i=i-1
      yield
    end
  end
end

3.my_times{
  puts 'using yield and block'
}

# call block

def call_block(&block)
  block.call
  
end
