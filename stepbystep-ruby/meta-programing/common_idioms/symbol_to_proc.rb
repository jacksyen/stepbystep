names = ['bob', 'bill', 'heather']
names.map {|name| name.capitalize }   # => ["Bob", "Bill", "Heather"]

class Symbol
  def to_proc
    Proc.new {|x| x.send(self) }
  end
end

names = ['bob', 'bill', 'heather']
names.map(&:capitalize.to_proc)   # => ["Bob", "Bill", "Heather"]

require_relative '../assertion.rb'
assert_equals %w(Bob Bill Heather), names.map(&:capitalize.to_proc)

names = %w(bob bill heather)
names.map(&:capitalize)   # => ["Bob", "Bill", "Heather"]

assert_equals %w(Bob Bill Heather), names.map(&:capitalize)
