class SalesDataFeed
  def initialize
    @items=[]
  end

  def add_sales_item(isbn,amount)
    @items <<BookInStock.new(isbn,amount)
  end

  def total_sales
    @items.inject(0,0){|sum,item| sum+item.amount}
  end

  def print_plain_text_data
    @items.each do |item|
      printf ("%-10s %10.2f \n",item.isbn,item.amount)

    end

    print(" ==============\n")
    print("%21.2f\n",total_sales)
  end
end

class CsvDataFeed < SalesDataFeed
  require 'csv'

  def initialize(csv_file_name)
    super()
    CSV.foreach(csv_file_name,headers:true)do |row|
      add_sales_item(row["isbn"],row["amount"])
    end
  end
end



feed = CsvDataFeed.new("data.csv")

puts feed.total_sales