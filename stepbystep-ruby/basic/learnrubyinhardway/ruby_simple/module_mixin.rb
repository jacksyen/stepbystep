# ================
# Modules
# ================

module Foo
  # ...
end

class Bar
  include Foo # if you want Foo as instance methods
  extend Foo  #
end

module PaymentSystem
  def included(klass)
    klass.extend()
  end

  #instance methods
  def pay
    # pay
  end

  module ClassMethods
    def probation
      # find people who are on probation
    end
  end
end

class Employee
  include PaymentSystem
end

