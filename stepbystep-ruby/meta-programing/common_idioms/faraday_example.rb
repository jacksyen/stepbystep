require 'faraday'

conn = Faraday.new("https://twitter.com/search") do |faraday|
  faraday.response      :logger
  faraday.adapter       Faraday.default_adapter
  faraday.params["q"]   = "ruby"
  faraday.params["src"] = "typd"
end

response = conn.get
response.status           # => 200

require_relative '../assertion.rb'
assert_equals 200, response.status
