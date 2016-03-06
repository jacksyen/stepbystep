module VanityPuts
  refine Object do
    private
    def puts(*args)
      args.each do |arg|
        Kernel::puts("Patrick Says: #{arg}")
      end
    end
  end
end

class PatrickStuff
  using VanityPuts

  def greeting(msg)
    puts msg
  end

end

puts "calling patrickstuff"
PatrickStuff.new.greeting("in PatrickStuff")
puts "back"