class Die
  include Enumerable

  def each
    loop do
      yield rand(6)+1
    end
  end
end


d = Die.new
d.each do |roll|
  puts "you rolled a #{roll}"
  if roll==6
    puts "You Win"
    break
  end
end