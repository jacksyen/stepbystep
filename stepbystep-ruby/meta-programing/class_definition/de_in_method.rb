class C
  def m1
    def m2

    end
  end
end

class D < C

end

obj = D.new
obj.m1

C.instance_methods(false)

require_relative '../test/assertions'
assert_equal [:m1,:m2],C.instance_methods(false)