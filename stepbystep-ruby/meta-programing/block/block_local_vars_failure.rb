def just_yield
  yield
end

top_level_variable = 1
# local_to_block=0

just_yield do
  top_level_variable += 1
  local_to_block = 1
end

p top_level_variable  # => 2
# p local_to_block      # => Error!