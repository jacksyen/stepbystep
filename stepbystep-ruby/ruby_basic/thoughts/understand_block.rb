# First-class function and Higher-order function

# First-class function
#  Ruby 的 block 的本质：高阶函数的函数参数的变体。
a = ["a","b","c"]
puts a.map {|e| e+"!"}
puts(a)
puts a.reduce {|n1,n2| n1+n2}

# def test(func)
#   func()
# end
#
# def test2
#   puts "this is test2"
# end
#
# test(test2)

# higher-order function 一般翻译成高阶函数，是指接受函数做参数或者返回函数的函数。

#Ruby 里，函数不是一等公民，没有 first-class functions。
# 但是在 Ruby 里怎样使用高阶函数呢？答案就是使用 block。
#可以直接用 block，也可以用 lambda 或者 proc 把 block 转换成 Proc 类的实例用。

name="patrick"
def greet(name)
  puts "hello #{name}"
end

greet(name)

# use block
define_method(:greet_1) do
  puts "hello #{name}"
end

greet_1

def hello
  (1..10).each {|e| return e}
  return "hello"
end

puts hello