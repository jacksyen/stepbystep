def fibonacci_sequence
  Enumerator.new do |generator|
    i1,i2=1,1
    loop do
      generator.yield i1
      i1,i2 =i2,i1+i2
    end
  end
end

fibonacci_sequence