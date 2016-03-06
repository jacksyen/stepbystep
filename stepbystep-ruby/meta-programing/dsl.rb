require 'markaby'

html = Markaby::Builder.new do
  head { title "My wonderful home page" }
  body do
    h1 "Welcome to my home page!"
    b "My hobbies:"
    ul do
      li "Juggling"
      li "Knitting"
      li "Metaprogramming"
    end
  end
end
