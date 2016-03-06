im = BasicObject.instance_methods

p im

require_relative '../assertion.rb'

assert_equals [:==, :equal?, :!, :!=, :instance_eval, :instance_exec, :__send__, :__id__], BasicObject.instance_methods