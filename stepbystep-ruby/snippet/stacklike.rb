class String
	def ^(key)
		kenum =key.bytes.cycle
		bytes.map { |byte| byte^ kenum.next }.pack("C*")
  end
end

puts "testing".^("s")