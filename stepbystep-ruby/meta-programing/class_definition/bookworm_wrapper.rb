class Amazon
  def reviews_of(book)
    ['one','two','three']
  end
end

module AmazonWrapper
  def reviews_of(book)
    start =Time.now
    result =super
    time_taken=Time.now-start
    puts "reviews_of() took more tha #{time_taken}"
    puts result
    result
  rescue
    puts "reviews_of() failed"
    []
  end
end

Amazon.class_eval do
  prepend AmazonWrapper
end

def deserves_a_look?(book)
  amazon = Amazon.new
  amazon.reviews_of(book)
end

require_relative '../test/assertions'
assert_false deserves_a_look? Object.new