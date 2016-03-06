module M
  class C
    X = 'a constant'
  end
  C::X # => "a constant"
end

M::C::X # => "a constant"

Y = 'a root-level constant'

module M
  Y = 'a constant in M'
  Y      # => "a constant in M"
  ::Y    # => "a root-level constant"
end

M.constants                        # => [:C, :Y]
Module.constants.include? :Object  # => true
Module.constants.include? :Module  # => true

module M
  class C
    module M2
      Module.nesting    # => [M::C::M2, M::C, M]
    end
  end
end

require_relative "../assertion.rb"

assert_equals [:C, :Y], M.constants
assert Module.constants.include? :Object
assert Module.constants.include? :Module

assert_equals "a constant", M::C::X

module M
  class C
    assert_equals "a constant in M", ::M::Y

    module M2
      assert_equals [M::C::M2, M::C, M], Module.nesting
    end
  end
  assert_equals "a constant", C::X
end

module MyModule
  MyConstant = 'Outer constant'

  class MyClass
    MyConstant = 'Inner constant'
  end
end

module M1
  def my_method
    'M1#my_method()'
  end
end

class C
  include M1
end

class D < C; end

D.ancestors # => [D, C, M1, Object, Kernel, BasicObject]

assert_equals [D, C, M1, Object, Kernel, BasicObject], D.ancestors

module M1; end

module M2
  include M1
end

module M3
  prepend M1
  include M2
end

M3.ancestors # => [M1, M3, M2]

assert_equals [M1, M3, M2], M3.ancestors

module M2
  def my_method
    'M2#my_method()'
  end
end

class C2
  prepend M2
end

class D2 < C2; end

D2.ancestors # => [D2, M2, C2, Object, Kernel, BasicObject]

assert_equals [D2, M2, C2, Object, Kernel, BasicObject], D2.ancestors

module StringExtensions
  refine String do
    def to_alphanumeric
      gsub(/[^\w\s]/, '')
    end
  end
end

using StringExtensions

"my *1st* refinement!".to_alphanumeric  # => "my 1st refinement"

assert_equals "my 1st refinement", "my *1st* refinement!".to_alphanumeric

module StringExtensions
  refine String do
    def reverse
      "esrever"
    end
  end
end

module StringStuff
  using StringExtensions
  "my_string".reverse    # => "esrever"

  assert_equals "esrever", "my_string".reverse
end

"my_string".reverse      # => "gnirts_ym"

assert_equals "gnirts_ym", "my_string".reverse
