require 'net/http'

pages = %w(www.soso.com www.baidu.com)

threads = pages.map do |page|
  Thread.new(page) do |url|
    http=Net::HTTP.new(url,80)
    print "Fetching: #{url} \n"
    resp= http.get("/")
    print "Got #{url}: #{resp.message}"
  end
end

threads.each { |thr| thr.join}