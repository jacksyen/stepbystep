begin
  class Lawyer;
  end
  nick = Lawyer.new
  nick.talk_simple
rescue Exception => e
  p e
  # NoMethodError: undefined method `talk_simple' for #<Lawyer:0x007f801aa81938>
end

begin
  nick.send :method_missing, :my_method
rescue Exception => e
  p e
  # NoMethodError: undefined method `my_method' for #<Lawyer:0x007f801b0f4978>
end
