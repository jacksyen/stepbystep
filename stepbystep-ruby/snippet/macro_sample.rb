class Movie
  puts "inside class definition of #{self}"

  def self.my_class_method
    puts "running class method...."
  end

  def self.has_many(name)
    puts "#{self} has many #{name}"
    define_method(name) do
      puts "select * from #{name} where....."
      puts "Returning #{name}"
      []
    end
  end

  has_many :reviews
end


m = Movie.new
m.reviews