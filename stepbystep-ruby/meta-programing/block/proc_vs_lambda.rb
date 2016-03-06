def double(callable_object)
  callable_object.call * 2
end

l = lambda { return 20 }

p double(l)

def another_double
  p = Proc.new { return 10 }
  result = p.call
  return result * 2 ## unreachable code
end

p another_double

p = Proc.new { return 10 }
begin
  double(p) # LocalJumpError
rescue
end

proc = Proc.new { 10 }
p double(proc)

p.arity  # => 2




