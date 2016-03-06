# Inherit from struct
Person = Struct.new(:name,:like) do
  def to_s
    "#{self.name} likes #{self.like}"
  end
end

dave =Person.new('dave', 'ruby')
p dave
puts(dave)