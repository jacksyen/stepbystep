inc = Proc.new {|x| x+1}
inc.call(2)

dec = lambda {|x| x-1}
p dec.class
p dec.call(2)

