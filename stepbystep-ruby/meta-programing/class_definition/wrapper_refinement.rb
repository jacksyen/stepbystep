module StringRefinement
  refine String do
    def length
      super > 5 ? 'long' : 'short'
    end
  end
end

using StringRefinement

'War and Peace'.length      # => "long"

require_relative '../assertion.rb'
assert_equals 'long', 'War and Peace'.length