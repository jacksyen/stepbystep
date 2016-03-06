class Rainbow
  include Enumerable
  def each
    yield "red"
    yield "orange"
    yield "yello"
    yield "blue"
    yield "indigo"
    yield "violet"
  end
end

r = Rainbow.new
r.each do |color|
  puts "Next color: #{color}"
end
