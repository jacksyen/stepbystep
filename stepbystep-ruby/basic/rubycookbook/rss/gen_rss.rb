require 'rss/0.9'

rss = RSS::Rss.new("0.9")
channel = RSS::Rss::Channel.new

channel.title = "The Daily Patrick"
channel.description = "Patrick's Feed"
channel.language = "zh-cn"
channel.link = "http://www.simonpatrick.com"
rss.channel = channel

image = RSS::Rss::Channel::Image.new
image.url = "http://www.simonpatrick.com/simonpatrick.gif"
image.link= channel.link
channel.image = image

3.times do|i|
  item = RSS::Rss::Channel::Item.new
  item.title = "My News Number #{i}"
  item.link ="http://www.simonpatrick.com"
  item.description = "This is a story about number #{i}"
  channel.items << item
end

puts rss.to_s
