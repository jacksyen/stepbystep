class MyClass

end

def MyClass.a_class_method

end

class MyClass
  def self.another_class_method

  end
end

class MyClass
  class << self
    def yet_another_class_method

    end
  end
end

require_relative '../test/assertions'
assert MyClass.methods(false).include?(:a_class_method)
assert MyClass.methods(false).include?(:another_class_method)
assert MyClass.methods(false).include?(:yet_another_class_method)
