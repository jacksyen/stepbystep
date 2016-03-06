re = %r{(?:(read)|blue) ball and (blue|red) bucket}

puts re.match("red ball and blue bucket")
puts re.match("blue ball and red bucket")


def show_regexp(string,pattern)
  match = pattern.match(string)
  if match
    "#{match.pre_match}->#{match[0]}<-#{match.post_match}}"
  else
    "no match"
  end
end