require 'rss/2.0'
require 'open-uri'

open("https://ruby-lang.org/en/feeds/news.rss") do |http|
  response =http.read
  result = RSS::Parser.parse(response,false)
  puts "Channel: " +result.channel.title
  result.items.each_with_index do |item,i|
    puts "#{i+1}.#{item.title}" if i<3
  end
end