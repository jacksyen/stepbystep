class Lawyer
  def method_missing(method, *args)
    puts "You called: #{method}(#{args.join(', ')})"
    puts '(You also passed it a block)' if block_given?
  end
end

bob = Lawyer.new
bob.talk_simple('a', 'b') do
  # a block
  puts 'a'+'b'
end

class Roulette
  def method_missing(name, *args)
    person = name.to_s.capitalize
    puts person
    super unless %w[Bob Frank Bill].include? person
    3.times do
      number = rand(10) + 1
      puts "#{number}..."
    end
  end
end

number_of = Roulette.new
puts number_of.bill
