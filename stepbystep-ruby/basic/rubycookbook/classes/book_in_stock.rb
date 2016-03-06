class BookInStock
  attr_reader :isbn,:price
  def initialize(isbn,price)
    @isbn = isbn
    @price = Float(price)
  end

  def price=(new_price)
    @price = new_price
  end
end

b = BookInStock.new("ISBN0001",45.0)
b.price=45.99
puts b.isbn
puts b.price