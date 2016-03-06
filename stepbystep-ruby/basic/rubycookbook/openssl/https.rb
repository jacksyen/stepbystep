require 'net/https'

USER = "xxx"
PW = "yyy"

site = Net::HTTP.new("www.baidu.com",443)
site.use_ssl =true
response = site.get2("/",'Authorization' => 'Basic' +["#{USER}:#{PW}"].pack('m').strip)

puts response