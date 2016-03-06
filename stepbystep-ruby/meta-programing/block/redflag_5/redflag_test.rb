
# add this folder to the load path
$: << File.expand_path(File.dirname(__FILE__))

# hack Kernel#puts
$PUTS = []
module Kernel
  alias_method :old_puts, :puts
  def puts(s); $PUTS << s; end
end

# setup test
require_relative 'redflag.rb'

# de-hack Kernel#puts
module Kernel
  alias_method :puts, :old_puts
end

# remove this folder from load path
$:.pop

# test!
expected = [
    "Setting up sky",
    "Setting up mountains",
    "ALERT: the sky is falling",
    "Setting up sky",
    "Setting up mountains",
    "ALERT: it's getting closer",
    "Setting up sky",
    "Setting up mountains"
]
puts expected, $PUTS
