$PUTS=[]

$:<<File.expand_path(File.dirname(__FILE__))

# hack Kernel#puts
module Kernel
  alias_method :old_puts, :puts
  def puts(s)
    $PUTS<<s
  end
end

require_relative('redflag.rb')

#de-hack Kernel#puts
module Kernel
  alias_method :puts, :old_puts
end

$:.pop

puts $PUTS