
# add this folder to load path
$: << File.expand_path(File.dirname(__FILE__))

$PUTS=[]

module Kernel
  alias_method :old_puts, :puts
  def puts(s)
    $PUTS<<s
  end
end

require_relative('redflag.rb')

module Kernel
  alias_method :puts, :old_puts
end

# remove this folder from load path
#:.pop

puts $PUTS