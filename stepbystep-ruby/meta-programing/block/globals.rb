
# $ as global variable

def a_scope
  $var = "some value"
end

def another_scope
  $var
end

p a_scope
p another_scope