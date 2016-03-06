class Object
  attr_accessor :timestamp
end

class Class
  old_new = instance_method :new
  define_method :new do |*args,&block|
    result = old_new.bind(self).call(*args,&block)
    result.timestamp = Time.now
    result
  end
end

puts Class.new.timestamp