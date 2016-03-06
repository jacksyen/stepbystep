class Object
  def tap
    yield self
    self
  end
end

%w(a b c).push('d').shift.upcase.next # => "B"

temp = %w(a b c).push('d').shift
puts temp
x = temp.upcase.next

%w(a b c).push('d').shift.tap {|x| puts x }.upcase.next