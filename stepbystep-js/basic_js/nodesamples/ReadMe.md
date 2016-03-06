# Node notes

## Express

## benchmark

[js-perf](http://jsperf.com/math-perf-alsotang)

## 作用域与闭包

作用域与闭包：this，var，(function () {})

## Javascript OOP
js 是面向对象的，但是是“基于原型的面向对象”，没有类。没有多重继承，没有接口。没有结构体，没有枚举类型。
但它的字面量哈希和 function 都足够灵活，拼拼凑凑，上面那些东西都能“模拟”着用。

## callback hell
使用eventproxy，async已经可以解决大部分问题

参见：

* 《使用 eventproxy 控制并发》：https://github.com/alsotang/node-lessons/tree/master/lesson4
* 《使用 async 控制并发》：https://github.com/alsotang/node-lessons/tree/master/lesson5


### 函数式编程

js 中，匿名函数非常的方便，有效利用函数式编程的特性可以使人写代码时心情愉悦。

使用 lodash：https://lodash.com/docs

### 设计模式

《解密设计模式-王垠》

https://github.com/alsotang/node-lessons/blob/master/lesson14/%E8%A7%A3%E5%A