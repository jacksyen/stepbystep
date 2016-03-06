# 《搭建 Node.js 开发环境》

本课程假设大家都是在 Linux 或者 Mac 下面。至于使用 Windows 并坚持玩新技术的同学，我坚信他们一定有着过人的、甚至是不可告人的兼容性 bug 处理能力，所以这部分同学麻烦在课程无法继续时，自行兼容一下。

不久前公司刚发一台新 Mac 给我，所以我对于在新环境中安装 Node.js 的过程还是记忆犹新的。

其实这过程特别简单:

### 先安装一个 nvm（ https://github.com/creationix/nvm ）

```
$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.25.2/install.sh | bash
```

nvm 的全称是 **Node Version Manager**，之所以需要这个工具，是因为 Node.js 的各种特性都没有稳定下来，所以我们经常由于老项目或尝新的原因，需要切换各种版本。

安装完成后，你的 shell 里面应该就有个 nvm 命令了，调用它试试

```
$ nvm
```

当看到有输出时，则 nvm 安装成功。

### 安装 Node.js

使用 nvm 的命令安装 Node.js 最新稳定版，现在是 `v0.12.3`。

```
$ nvm install 0.12
```

安装完成后，查看一下

```
$ nvm ls
```

这时候可以看到自己安装的所有 Node.js 版本，输出应如下：

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson0/1.png)

（图1）

那个绿色小箭头的意思就是现在正在使用的版本，我这里是 `v0.10.29`。我还安装了 `v0.11.14`，但它并非我当前使用的版本。

如果你那里没有出现绿色小箭头的话，告诉 nvm 你要使用 `0.12.x` 版本

```
$ nvm use 0.12
```

然后再次查看，这时候小箭头应该出现了。

OK，我们在终端中输入

```
$ node
```

REPL(read–eval–print loop) 应该就出来了，那我们就成功了。

随便敲两行命令玩玩吧。

比如 `> while (true) {}`，这时你的 CPU 应该会飚高。

### 完善安装

上述过程完成后，有时会出现，当开启一个新的 shell 窗口时，找不到 node 命令的情况。

这种情况一般来自两个原因

一、shell 不知道 nvm 的存在

二、nvm 已经存在，但是没有 default 的 Node.js 版本可用。

解决方式：

一、检查 `~/.profile` 或者 `~/.bash_profile` 中有没有这样两句

```
export NVM_DIR="/Users/YOURUSERNAME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm
```

没有的话，加进去。

这两句会在 bash 启动的时候被调用，然后注册 nvm 命令。

二、

调用

`$ nvm ls`

看看像不像上述图1中一样，有 default 的指向。

如果没有的话，执行

`$ nvm alias default 0.12`

再

`$ nvm ls`

看一下


# 《一个最简单的 express 应用》

## 目标

建立一个 lesson1 项目，在其中编写代码。当在浏览器中访问 `http://localhost:3000/` 时，输出 `Hello World`。

## 挑战

访问 `http://localhost:3000/` 时，输出 `你好，世界`。

## 知识点

1. 包管理器 npm 。使用 npm 安装包，并自动安装所需依赖。
2. 框架 express 。学习新建 express 实例，并定义 routes ，产生输出。

## 课程内容

按照惯例，我们来个 helloworld 入门。

### 包管理器 npm

npm 可以自动管理包的依赖. 只需要安装你想要的包, 不必考虑这个包的依赖包.

在 PHP 中, 包管理使用的 `Composer`, python 中，包管理使用 `easy_install` 或者 `pip`，ruby 中我们使用 `gem`。而在 Node.js 中，对应就是 `npm`，npm 是 `Node.js Package Manager` 的意思。

### 框架 Express

express 是 Node.js 应用最广泛的 web 框架，现在是 4.x 版本，它非常薄。跟 Rails 比起来，完全两个极端。

express 的官网是 http://expressjs.com/ ，我常常上去看它的 API。

首先我们需要得到一个 express。

不同于 ruby 的 gem 装在全局，Node.js 的依赖是以项目为单位管理的，直接就安装在项目的 `node_modules` 目录下，而且每个依赖都可以有指定版本的其他依赖，这些依赖像一棵树一样。根据我自己的使用经验来说，npm 的体验在 pip 和 gem 之上。

OK，新建一个文件夹叫 lesson1 的，进去里面安装 express

```
$ mkdir lesson1 && cd lesson1
# 这里没有从官方 npm 安装，而是使用了大淘宝的 npm 镜像
$ npm install express --registry=https://registry.npm.taobao.org
```

安装完成后，我们的 lesson1 目录下应该会出现一个 `node_modules` 文件夹，`ls` 看看

```
$ ls node_modules
```

里面如果出现 express 文件夹则说明安装成功。

或者 npm命令提供更清晰直观的显示:
```
$ npm list
```

我们继续应用程序的编写。

新建一个 app.js 文件

```
$ touch app.js
```

copy 进去这些代码

```js
// 这句的意思就是引入 `express` 模块，并将它赋予 `express` 这个变量等待使用。
var express = require('express');
// 调用 express 实例，它是一个函数，不带参数调用时，会返回一个 express 实例，将这个变量赋予 app 变量。
var app = express();

// app 本身有很多方法，其中包括最常用的 get、post、put/patch、delete，在这里我们调用其中的 get 方法，为我们的 `/` 路径指定一个 handler 函数。
// 这个 handler 函数会接收 req 和 res 两个对象，他们分别是请求的 request 和 response。
// request 中包含了浏览器传来的各种信息，比如 query 啊，body 啊，headers 啊之类的，都可以通过 req 对象访问到。
// res 对象，我们一般不从里面取信息，而是通过它来定制我们向浏览器输出的信息，比如 header 信息，比如想要向浏览器输出的内容。这里我们调用了它的 #send 方法，向浏览器输出一个字符串。
app.get('/', function (req, res) {
  res.send('Hello World');
});

// 定义好我们 app 的行为之后，让它监听本地的 3000 端口。这里的第二个函数是个回调函数，会在 listen 动作成功后执行，我们这里执行了一个命令行输出操作，告诉我们监听动作已完成。
app.listen(3000, function () {
  console.log('app is listening at port 3000');
});
```

执行

`$ node app.js`

这时候我们的 app 就跑起来了，终端中会输出 `app is listening at port 3000`。这时我们打开浏览器，访问 `http://localhost:3000/`，会出现 `Hello World`。如果没有出现的话，肯定是上述哪一步弄错了，自己调试一下。

## 补充知识

在这个例子中，node代码监听了3000端口，用户通过访问`http://localhost:3000/` 得到了内容，为什么呢？

### 端口

端口的作用：`通过端口来区分出同一电脑内不同应用或者进程，从而实现一条物理网线(通过分组交换技术-比如internet)同时链接多个程序`
[Port_(computer_networking)](http://en.wikipedia.org/wiki/Port_(computer_networking))

端口号是一个 16位的 uint, 所以其范围为 1 to 65535 (对TCP来说, port 0 被保留，不能被使用. 对于UDP来说, source端的端口号是可选的， 为0时表示无端口).

`app.listen(3000)`，进程就被打标，电脑接收到的3000端口的网络消息就会被发送给我们启动的这个进程

### URL

[RFC1738](http://www.ietf.org/rfc/rfc1738.txt) 定义的url格式笼统版本`<scheme>:<scheme-specific-part>`，
scheme有我们很熟悉的`http`、`https`、`ftp`，以及著名的`ed2k`，`thunder`。

通常我们熟悉的url定义成这个样子
```
<scheme>://<user>:<password>@<host>:<port>/<url-path>
```
用过ftp的估计能体会这么长的，网页上很少带auth信息，所以就精简成这样:
```
<scheme>://<host>:<port>/<url-path>
```
在上面的例子中, scheme=http, host=localhost, port=3000, url-path=/, 再联想对照一下浏览器端`window.location`对象。
著名的`localhost`，你可以在电脑的hosts文件上找到

[在这篇文章中提到](http://en.wikipedia.org/wiki/URI_scheme)： `URI schemes are frequently and incorrectly referred to as "protocols", or specifically as URI protocols or URL protocols, since most were originally designed to be used with a particular protocol, and often have the same name`，比较认同这个观点，尤其是今天移动设备的时代里， android和ios的开发中大量使用uri作为跨app通讯通道，把scheme理解为协议略狭隘了。

### 尾声

在了解完端口和url之后，再去看例子代码，相信应该好理解很多。
有必要的话，还可以在解刨一下express的use逻辑，对峙`http.createServer`，相信还有火花，:)


# 《学习使用外部模块》

## 目标

建立一个 lesson2 项目，在其中编写代码。

当在浏览器中访问 `http://localhost:3000/?q=alsotang` 时，输出 `alsotang` 的 md5 值，即 `bdd5e57b5c0040f9dc23d430846e68a3`。

## 挑战

访问 `http://localhost:3000/?q=alsotang` 时，输出 `alsotang` 的 sha1 值，即 `e3c766d71667567e18f77869c65cd62f6a1b9ab9`。

## 知识点

1. 学习 req.query 的用法
2. 学习建立 package.json 来管理 Node.js 项目。

## 课程内容

卧槽，不写 package.json 就写项目我觉得好不爽啊，所以这个 lesson2 我就得跟大家介绍一下 package.json 这个文件的用法了。

简单说来呢，这个 package.json 文件就是定义了项目的各种元信息，包括项目的名称，git repo 的地址，作者等等。最重要的是，其中定义了我们项目的依赖，这样这个项目在部署时，我们就不必将 `node_modules` 目录也上传到服务器，服务器在拿到我们的项目时，只需要执行 `npm install`，则 npm 会自动读取 package.json 中的依赖并安装在项目的 `node_modules` 下面，然后程序就可以在服务器上跑起来了。

本课程的每个 lesson 里面的示例代码都会带上一份 package.json，大家可以去看看它的大概样子。

我们来新建一个 lesson2 项目，并生成一份它的 package.json。

```
$ mkdir lesson2 && cd lesson2
$ npm init
```

OK，这时会要求我们输入一些信息，乱填就好了，反正这个地方也不用填依赖关系。

`npm init` 这个命令的作用就是帮我们互动式地生成一份最简单的 package.json 文件，`init` 是 `initialize` 的意思，初始化。

当乱填信息完毕之后，我们的目录下就会有个 package.json 文件了。

这时我们来安装依赖，这次的应用，我们依赖 `express` 和 `utility` 两个模块。

`$ npm install express utility --save`

这次的安装命令与上节课的命令有两点不同，一是没有指定 registry，没有指定的情况下，默认从 npm 官方安装，上次我们是从淘宝的源安装的。二是多了个 `--save` 参数，这个参数的作用，就是会在你安装依赖的同时，自动把这些依赖写入 package.json。命令执行完成之后，查看 package.json，会发现多了一个 `dependencies` 字段，如下图：

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson2/1.png)

这时查看 `node_modules` 目录，会发现有两个文件夹，分别是 express 和 utility

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson2/2.png)

我们开始写应用层的代码，建立一个 `app.js` 文件，复制以下代码进去：

```js
// 引入依赖
var express = require('express');
var utility = require('utility');

// 建立 express 实例
var app = express();

app.get('/', function (req, res) {
  // 从 req.query 中取出我们的 q 参数。
  // 如果是 post 传来的 body 数据，则是在 req.body 里面，不过 express 默认不处理 body 中的信息，需要引入 https://github.com/expressjs/body-parser 这个中间件才会处理，这个后面会讲到。
  // 如果分不清什么是 query，什么是 body 的话，那就需要补一下 http 的知识了
  var q = req.query.q;

  // 调用 utility.md5 方法，得到 md5 之后的值
  // 之所以使用 utility 这个库来生成 md5 值，其实只是习惯问题。每个人都有自己习惯的技术堆栈，
  // 我刚入职阿里的时候跟着苏千和朴灵混，所以也混到了不少他们的技术堆栈，仅此而已。
  // utility 的 github 地址：https://github.com/node-modules/utility
  // 里面定义了很多常用且比较杂的辅助方法，可以去看看
  var md5Value = utility.md5(q);

  res.send(md5Value);
});

app.listen(3000, function (req, res) {
  console.log('app is running at port 3000');
});

```

OK，运行我们的程序

`$ node app.js`

访问 `http://localhost:3000/?q=alsotang`，完成。

## 题外话

如果直接访问 `http://localhost:3000/` 会抛错

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson2/3.png)

可以看到，这个错误是从 `crypto.js` 中抛出的。

这是因为，当我们不传入 `q` 参数时，`req.query.q` 取到的值是 `undefined`，`utility.md5` 直接使用了这个空值，导致下层的 `crypto` 抛错。

# 《使用 superagent 与 cheerio 完成简单爬虫》

## 目标

建立一个 lesson3 项目，在其中编写代码。

当在浏览器中访问 `http://localhost:3000/` 时，输出 CNode(https://cnodejs.org/ ) 社区首页的所有帖子标题和链接，以 json 的形式。

输出示例：

```js
[
  {
    "title": "【公告】发招聘帖的同学留意一下这里",
    "href": "http://cnodejs.org/topic/541ed2d05e28155f24676a12"
  },
  {
    "title": "发布一款 Sublime Text 下的 JavaScript 语法高亮插件",
    "href": "http://cnodejs.org/topic/54207e2efffeb6de3d61f68f"
  }
]

```

## 挑战

访问 `http://localhost:3000/` 时，输出包括主题的作者，

示例：

```js
[
  {
    "title": "【公告】发招聘帖的同学留意一下这里",
    "href": "http://cnodejs.org/topic/541ed2d05e28155f24676a12",
    "author": "alsotang"
  },
  {
    "title": "发布一款 Sublime Text 下的 JavaScript 语法高亮插件",
    "href": "http://cnodejs.org/topic/54207e2efffeb6de3d61f68f",
    "author": "otheruser"
  }
]
```

## 知识点

1. 学习使用 superagent 抓取网页
2. 学习使用 cheerio 分析网页

## 课程内容

Node.js 总是吹牛逼说自己异步特性多么多么厉害，但是对于初学者来说，要找一个能好好利用异步的场景不容易。我想来想去，爬虫的场景就比较适合，没事就异步并发地爬几个网站玩玩。

本来想教大家怎么爬 github 的 api 的，但是 github 有 rate limit 的限制，所以只好牺牲一下 CNode 社区（国内最专业的 Node.js 开源技术社区），教大家怎么去爬它了。

我们这回需要用到三个依赖，分别是 express，superagent 和 cheerio。

先介绍一下，

superagent(http://visionmedia.github.io/superagent/ ) 是个 http 方面的库，可以发起 get 或 post 请求。

cheerio(https://github.com/cheeriojs/cheerio ) 大家可以理解成一个 Node.js 版的 jquery，用来从网页中以 css selector 取数据，使用方式跟 jquery 一样一样的。

还记得我们怎么新建一个项目吗？

1. 新建一个文件夹，进去之后 `npm init`
1. 安装依赖 `npm install --save PACKAGE_NAME`
1. 写应用逻辑

我们应用的核心逻辑长这样

```js
app.get('/', function (req, res, next) {
  // 用 superagent 去抓取 https://cnodejs.org/ 的内容
  superagent.get('https://cnodejs.org/')
    .end(function (err, sres) {
      // 常规的错误处理
      if (err) {
        return next(err);
      }
      // sres.text 里面存储着网页的 html 内容，将它传给 cheerio.load 之后
      // 就可以得到一个实现了 jquery 接口的变量，我们习惯性地将它命名为 `$`
      // 剩下就都是 jquery 的内容了
      var $ = cheerio.load(sres.text);
      var items = [];
      $('#topic_list .topic_title').each(function (idx, element) {
        var $element = $(element);
        items.push({
          title: $element.attr('title'),
          href: $element.attr('href')
        });
      });

      res.send(items);
    });
});
```

OK，一个简单的爬虫就是这么简单。这里我们还没有利用到 Node.js 的异步并发特性。不过下两章内容都是关于异步控制的。

记得好好看看 superagent 的 API，它把链式调用的风格玩到了极致。


# 《使用 eventproxy 控制并发》

## 目标

建立一个 lesson4 项目，在其中编写代码。

代码的入口是 `app.js`，当调用 `node app.js` 时，它会输出 CNode(https://cnodejs.org/ ) 社区首页的所有主题的标题，链接和第一条评论，以 json 的格式。

输出示例：

```js
[
  {
    "title": "【公告】发招聘帖的同学留意一下这里",
    "href": "http://cnodejs.org/topic/541ed2d05e28155f24676a12",
    "comment1": "呵呵呵呵"
  },
  {
    "title": "发布一款 Sublime Text 下的 JavaScript 语法高亮插件",
    "href": "http://cnodejs.org/topic/54207e2efffeb6de3d61f68f",
    "comment1": "沙发！"
  }
]
```

## 挑战

以上文目标为基础，输出 `comment1` 的作者，以及他在 cnode 社区的积分值。

示例：

```js
[
  {
    "title": "【公告】发招聘帖的同学留意一下这里",
    "href": "http://cnodejs.org/topic/541ed2d05e28155f24676a12",
    "comment1": "呵呵呵呵",
    "author1": "auser",
    "score1": 80
  },
  ...
]
```

## 知识点

1. 体会 Node.js 的 callback hell 之美
2. 学习使用 eventproxy 这一利器控制并发

## 课程内容

这一章我们来到了 Node.js 最牛逼的地方——异步并发的内容了。

上一课我们介绍了如何使用 superagent 和 cheerio 来取主页内容，那只需要发起一次 http get 请求就能办到。但这次，我们需要取出每个主题的第一条评论，这就要求我们对每个主题的链接发起请求，并用 cheerio 去取出其中的第一条评论。

CNode 目前每一页有 40 个主题，于是我们就需要发起 1 + 40 个请求，来达到我们这一课的目标。

后者的 40 个请求，我们并发地发起：），而且不会遇到多线程啊锁什么的，Node.js 的并发模型跟多线程不同，抛却那些观念。更具体一点的话，比如异步到底为何异步，Node.js 为何单线程却能并发这类走近科学的问题，我就不打算讲了。对于这方面有兴趣的同学，强烈推荐 @朴灵 的 《九浅一深Node.js》： http://book.douban.com/subject/25768396/ 。

有些逼格比较高的朋友可能听说过 promise 和 generator 这类概念。不过我呢，只会讲 callback，主要原因是我个人只喜欢 callback。

这次课程我们需要用到三个库：superagent cheerio eventproxy(https://github.com/JacksonTian/eventproxy )

手脚架的工作各位自己来，我们一步一步来一起写出这个程序。

首先 app.js 应该长这样

```js
var eventproxy = require('eventproxy');
var superagent = require('superagent');
var cheerio = require('cheerio');
// url 模块是 Node.js 标准库里面的
// http://nodejs.org/api/url.html
var url = require('url');

var cnodeUrl = 'https://cnodejs.org/';

superagent.get(cnodeUrl)
  .end(function (err, res) {
    if (err) {
      return console.error(err);
    }
    var topicUrls = [];
    var $ = cheerio.load(res.text);
    // 获取首页所有的链接
    $('#topic_list .topic_title').each(function (idx, element) {
      var $element = $(element);
      // $element.attr('href') 本来的样子是 /topic/542acd7d5d28233425538b04
      // 我们用 url.resolve 来自动推断出完整 url，变成
      // https://cnodejs.org/topic/542acd7d5d28233425538b04 的形式
      // 具体请看 http://nodejs.org/api/url.html#url_url_resolve_from_to 的示例
      var href = url.resolve(cnodeUrl, $element.attr('href'));
      topicUrls.push(href);
    });

    console.log(topicUrls);
  });
```

运行 `node app.js`

输出如下图：

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson4/1.png)

OK，这时候我们已经得到所有 url 的地址了，接下来，我们把这些地址都抓取一遍，就完成了，Node.js 就是这么简单。

抓取之前，还是得介绍一下 eventproxy 这个库。

用 js 写过异步的同学应该都知道，如果你要并发异步获取两三个地址的数据，并且要在获取到数据之后，对这些数据一起进行利用的话，常规的写法是自己维护一个计数器。

先定义一个 `var count = 0`，然后每次抓取成功以后，就 `count++`。如果你是要抓取三个源的数据，由于你根本不知道这些异步操作到底谁先完成，那么每次当抓取成功的时候，就判断一下 `count === 3`。当值为真时，使用另一个函数继续完成操作。

而 eventproxy 就起到了这个计数器的作用，它来帮你管理到底这些异步操作是否完成，完成之后，它会自动调用你提供的处理函数，并将抓取到的数据当参数传过来。

假设我们不使用 eventproxy 也不使用计数器时，抓取三个源的写法是这样的：

```js
// 参考 jquery 的 $.get 的方法
$.get("http://data1_source", function (data1) {
  // something
  $.get("http://data2_source", function (data2) {
    // something
    $.get("http://data3_source", function (data3) {
      // something
      var html = fuck(data1, data2, data3);
      render(html);
    });
  });
});
```

上述的代码大家都写过吧。先获取 data1，获取完成之后获取 data2，然后再获取 data3，然后 fuck 它们，进行输出。

但大家应该也想到了，其实这三个源的数据，是可以并行去获取的，data2 的获取并不依赖 data1 的完成，data3 同理也不依赖 data2。

于是我们用计数器来写，会写成这样：

```js
(function () {
  var count = 0;
  var result = {};

  $.get('http://data1_source', function (data) {
    result.data1 = data;
    count++;
    handle();
    });
  $.get('http://data2_source', function (data) {
    result.data2 = data;
    count++;
    handle();
    });
  $.get('http://data3_source', function (data) {
    result.data3 = data;
    count++;
    handle();
    });

  function handle() {
    if (count === 3) {
      var html = fuck(result.data1, result.data2, result.data3);
      render(html);
    }
  }
})();
```

<del>丑的一逼，</del>也不算丑，主要我写代码好看。

如果我们用 eventproxy，写出来是这样的：

```js
var ep = new eventproxy();
ep.all('data1_event', 'data2_event', 'data3_event', function (data1, data2, data3) {
  var html = fuck(data1, data2, data3);
  render(html);
});

$.get('http://data1_source', function (data) {
  ep.emit('data1_event', data);
  });

$.get('http://data2_source', function (data) {
  ep.emit('data2_event', data);
  });

$.get('http://data3_source', function (data) {
  ep.emit('data3_event', data);
  });
```

好看多了是吧，也就是个高等计数器嘛。

`ep.all('data1_event', 'data2_event', 'data3_event', function (data1, data2, data3) {});`

这一句，监听了三个事件，分别是 `data1_event, data2_event, data3_event`，每次当一个源的数据抓取完成时，就通过 `ep.emit()` 来告诉 `ep` 自己，某某事件已经完成了。

当三个事件未同时完成时，`ep.emit()` 调用之后不会做任何事；当三个事件都完成的时候，就会调用末尾的那个回调函数，来对它们进行统一处理。

eventproxy 提供了不少其他场景所需的 API，但最最常用的用法就是以上的这种，即：

1. 先 `var ep = new eventproxy();` 得到一个 eventproxy 实例。
1. 告诉它你要监听哪些事件，并给它一个回调函数。`ep.all('event1', 'event2', function (result1, result2) {})`。
1. 在适当的时候 `ep.emit('event_name', eventData)`。

eventproxy 这套处理异步并发的思路，我一直觉得就像是汇编里面的 goto 语句一样，程序逻辑在代码中随处跳跃。本来代码已经执行到 100 行了，突然 80 行的那个回调函数又开始工作了。如果你异步逻辑复杂点的话，80 行的这个函数完成之后，又激活了 60 行的另外一个函数。并发和嵌套的问题虽然解决了，但老祖宗们消灭了几十年的 goto 语句又回来了。

至于这套思想糟糕不糟糕，我个人倒是觉得还是不糟糕，用熟了看起来蛮清晰的。不过 js 这门渣渣语言本来就乱嘛，什么变量提升（http://www.cnblogs.com/damonlan/archive/2012/07/01/2553425.html ）啊，没有 main 函数啊，变量作用域啊，数据类型常常简单得只有数字、字符串、哈希、数组啊，这一系列的问题，都不是事儿。

编程语言美丑啥的，咱心中有佛就好。

回到正题，之前我们已经得到了一个长度为 40 的 `topicUrls` 数组，里面包含了每条主题的链接。那么意味着，我们接下来要发出 40 个并发请求。我们需要用到 eventproxy 的 `#after` API。

大家自行学习一下这个 API 吧：https://github.com/JacksonTian/eventproxy#%E9%87%8D%E5%A4%8D%E5%BC%82%E6%AD%A5%E5%8D%8F%E4%BD%9C

我代码就直接贴了哈。

```js
// 得到 topicUrls 之后

// 得到一个 eventproxy 的实例
var ep = new eventproxy();

// 命令 ep 重复监听 topicUrls.length 次（在这里也就是 40 次） `topic_html` 事件再行动
ep.after('topic_html', topicUrls.length, function (topics) {
  // topics 是个数组，包含了 40 次 ep.emit('topic_html', pair) 中的那 40 个 pair

  // 开始行动
  topics = topics.map(function (topicPair) {
    // 接下来都是 jquery 的用法了
    var topicUrl = topicPair[0];
    var topicHtml = topicPair[1];
    var $ = cheerio.load(topicHtml);
    return ({
      title: $('.topic_full_title').text().trim(),
      href: topicUrl,
      comment1: $('.reply_content').eq(0).text().trim(),
    });
  });

  console.log('final:');
  console.log(topics);
});

topicUrls.forEach(function (topicUrl) {
  superagent.get(topicUrl)
    .end(function (err, res) {
      console.log('fetch ' + topicUrl + ' successful');
      ep.emit('topic_html', [topicUrl, res.text]);
    });
});
```

输出长这样：

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson4/2.png)

完整的代码请查看 lesson4 目录下的 app.js 文件

# 《使用 async 控制并发》

## 目标

建立一个 lesson5 项目，在其中编写代码。

代码的入口是 `app.js`，当调用 `node app.js` 时，它会输出 CNode(https://cnodejs.org/ ) 社区首页的所有主题的标题，链接和第一条评论，以 json 的格式。

注意：与上节课不同，并发连接数需要控制在 5 个。

输出示例：

```js
[
  {
    "title": "【公告】发招聘帖的同学留意一下这里",
    "href": "http://cnodejs.org/topic/541ed2d05e28155f24676a12",
    "comment1": "呵呵呵呵"
  },
  {
    "title": "发布一款 Sublime Text 下的 JavaScript 语法高亮插件",
    "href": "http://cnodejs.org/topic/54207e2efffeb6de3d61f68f",
    "comment1": "沙发！"
  }
]
```

## 知识点

1. 学习 async(https://github.com/caolan/async ) 的使用。这里有个详细的 async demo 演示：https://github.com/alsotang/async_demo
1. 学习使用 async 来控制并发连接数。

## 课程内容

lesson4 的代码其实是不完美的。为什么这么说，是因为在 lesson4 中，我们一次性发了 40 个并发请求出去，要知道，除去 CNode 的话，别的网站有可能会因为你发出的并发连接数太多而当你是在恶意请求，把你的 IP 封掉。

我们在写爬虫的时候，如果有 1000 个链接要去爬，那么不可能同时发出 1000 个并发链接出去对不对？我们需要控制一下并发的数量，比如并发 10 个就好，然后慢慢抓完这 1000 个链接。

用 async 来做这件事很简单。

这次我们要介绍的是 async 的 `mapLimit(arr, limit, iterator, callback)` 接口。另外，还有个常用的控制并发连接数的接口是 `queue(worker, concurrency)`，大家可以去 https://github.com/caolan/async#queueworker-concurrency 看看说明。

这回我就不带大家爬网站了，我们来专注知识点：并发连接数控制。

对了，还有个问题是，什么时候用 eventproxy，什么时候使用 async 呢？它们不都是用来做异步流程控制的吗？

我的答案是：

当你需要去多个源(一般是小于 10 个)汇总数据的时候，用 eventproxy 方便；当你需要用到队列，需要控制并发数，或者你喜欢函数式编程思维时，使用 async。大部分场景是前者，所以我个人大部分时间是用 eventproxy 的。

正题开始。

首先，我们伪造一个 `fetchUrl(url, callback)` 函数，这个函数的作用就是，当你通过

```js
fetchUrl('http://www.baidu.com', function (err, content) {
  // do something with `content`
});
```

调用它时，它会返回 `http://www.baidu.com` 的页面内容回来。

当然，我们这里的返回内容是假的，返回延时是随机的。并且在它被调用时，会告诉你它现在一共被多少个地方并发调用着。

```js
// 并发连接数的计数器
var concurrencyCount = 0;
var fetchUrl = function (url, callback) {
  // delay 的值在 2000 以内，是个随机的整数
  var delay = parseInt((Math.random() * 10000000) % 2000, 10);
  concurrencyCount++;
  console.log('现在的并发数是', concurrencyCount, '，正在抓取的是', url, '，耗时' + delay + '毫秒');
  setTimeout(function () {
    concurrencyCount--;
    callback(null, url + ' html content');
  }, delay);
};
```

我们接着来伪造一组链接

```js
var urls = [];
for(var i = 0; i < 30; i++) {
  urls.push('http://datasource_' + i);
}
```

这组链接的长这样：

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson5/1.png)

接着，我们使用 `async.mapLimit` 来并发抓取，并获取结果。

```js
async.mapLimit(urls, 5, function (url, callback) {
  fetchUrl(url, callback);
}, function (err, result) {
  console.log('final:');
  console.log(result);
});
```

运行输出是这样的：

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson5/2.png)

可以看到，一开始，并发链接数是从 1 开始增长的，增长到 5 时，就不再增加。当其中有任务完成时，再继续抓取。并发连接数始终控制在 5 个。

完整代码请参见 app.js 文件。

# 《测试用例：mocha，should，istanbul》

## 目标

建立一个 lesson6 项目，在其中编写代码。

main.js: 其中有个 fibonacci 函数。fibonacci 的介绍见：http://en.wikipedia.org/wiki/Fibonacci_number 。

此函数的定义为 `int fibonacci(int n)`

* 当 n === 0 时，返回 0；n === 1时，返回 1;
* n > 1 时，返回 `fibonacci(n) === fibonacci(n-1) + fibonacci(n-2)`，如 `fibonacci(10) === 55`;
* n 不可大于10，否则抛错，因为 Node.js 的计算性能没那么强。
* n 也不可小于 0，否则抛错，因为没意义。
* n 不为数字时，抛错。

test/main.test.js: 对 main 函数进行测试，并使行覆盖率和分支覆盖率都达到 100%。

## 知识点

1. 学习使用测试框架 mocha : http://mochajs.org/
2. 学习使用断言库 should : https://github.com/tj/should.js
3. 学习使用测试率覆盖工具 istanbul : https://github.com/gotwarlost/istanbul
4. 简单 Makefile 的编写 : http://blog.csdn.net/haoel/article/details/2886

## 课程内容

首先，作为一个 Node.js 项目，先执行 `npm init` 创建 package.json。

其次，建立我们的 main.js 文件，编写 `fibonacci` 函数。

```js
var fibonacci = function (n) {
  if (n === 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }
  return fibonacci(n-1) + fibonacci(n-2);
};

if (require.main === module) {
  // 如果是直接执行 main.js，则进入此处
  // 如果 main.js 被其他文件 require，则此处不会执行。
  var n = Number(process.argv[2]);
  console.log('fibonacci(' + n + ') is', fibonacci(n));
}
```

OK，这只是个简单的实现。

我们可以执行试试

`$ node main.js 10`

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson6/1.png)

嗯，结果是 55，符合预期。

接下来我们开始测试驱动开发，现在简单的实现已经完成，那我们就对它进行一下简单测试吧。

我们先得把 main.js 里面的 fibonacci 暴露出来，这个简单。加一句

`exports.fibonacci = fibonacci;`（要是看不懂这句就去补补 Node.js 的基础知识吧）

就好了。

然后我们在 `test/main.test.js` 中引用我们的 main.js，并开始一个简单的测试。

```js
// file: test/main.test.js
var main = require('../main');
var should = require('should');

describe('test/main.test.js', function () {
  it('should equal 55 when n === 10', function () {
    main.fibonacci(10).should.equal(55);
  });
});
```

把测试先跑通，我们再讲这段测试代码的含义。

装个全局的 mocha: `$ npm install mocha -g`。

`-g` 与 非`-g` 的区别，就是安装位置的区别，g 是 global 的意思。如果不加的话，则安装 mocha 在你的项目目录下面；如果加了，则这个 mocha 是安装在全局的，如果 mocha 有可执行命令的话，那么这个命令也会自动加入到你系统 $PATH 中的某个地方（在我的系统中，是这里 `/Users/alsotang/.nvm/v0.10.29/bin`）

在 lesson6 目录下，直接执行

`$ mocha`

输出应如下

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson6/2.png)

那么，代码中的 describe 和 it 是什么意思呢？其实就是 BDD 中的那些意思，把它们当做语法来记就好了。

大家来看看 nodeclub 中，关于 topicController 的测试文件：

https://github.com/cnodejs/nodeclub/blob/master/test/controllers/topic.test.js

这文件的内容没有超出之前课程的范围吧。

`describe` 中的字符串，用来描述你要测的主体是什么；`it` 当中，描述具体的 case 内容。

而引入的那个 should 模块，是个断言库。玩过 ruby 的同学应该知道 `rspec`，rspec 它把测试框架和断言库的事情一起做了，而在 Node.js 中，这两样东西的作用分别是 mocha 和 should 在协作完成。

should 在 js 的 Object “基类”上注入了一个 `#should` 属性，这个属性中，又有着许许多多的属性可以被访问。

比如测试一个数是不是大于3，则是 `(5).should.above(3)`；测试一个字符串是否有着特定前缀：`'foobar'.should.startWith('foo');`。should.js API 在：https://github.com/tj/should.js

should.js 如果现在还是 version 3 的话，我倒是推荐大家去看看它的 API 和 源码；现在 should 是 version 4 了，API 丑得很，但为了不掉队，我还是一直用着它。我觉得 expect 麻烦，所以不用 expect，对了，expect 也是一个断言库：https://github.com/LearnBoost/expect.js/ 。

回到正题，还记得我们 fibonacci 函数的几个要求吗？

```
* 当 n === 0 时，返回 0；n === 1时，返回 1;
* n > 1 时，返回 `fibonacci(n) === fibonacci(n-1) + fibonacci(n-2)`，如 `fibonacci(10) === 55`;
* n 不可大于10，否则抛错，因为 Node.js 的计算性能没那么强。
* n 也不可小于 0，否则抛错，因为没意义。
* n 不为数字时，抛错。
```

我们用测试用例来描述一下这几个要求，更新后的 main.test.js 如下：

```js
var main = require('../main');
var should = require('should');

describe('test/main.test.js', function () {
  it('should equal 0 when n === 0', function () {
    main.fibonacci(0).should.equal(0);
  });

  it('should equal 1 when n === 1', function () {
    main.fibonacci(1).should.equal(1);
  });

  it('should equal 55 when n === 10', function () {
    main.fibonacci(10).should.equal(55);
  });

  it('should throw when n > 10', function () {
    (function () {
      main.fibonacci(11);
    }).should.throw('n should <= 10');
  });

  it('should throw when n < 0', function () {
    (function () {
      main.fibonacci(-1);
    }).should.throw('n should >= 0');
  });

  it('should throw when n isnt Number', function () {
    (function () {
      main.fibonacci('呵呵');
    }).should.throw('n should be a Number');
  });
});
```

还是比较清晰的吧？

我们这时候跑一下 `$ mocha`，会发现后三个 case 都没过。

于是我们更新 fibonacci 的实现：

```js
var fibonacci = function (n) {
  if (typeof n !== 'number') {
    throw new Error('n should be a Number');
  }
  if (n < 0) {
    throw new Error('n should >= 0')
  }
  if (n > 10) {
    throw new Error('n should <= 10');
  }
  if (n === 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }

  return fibonacci(n-1) + fibonacci(n-2);
};
```

再跑一次 `$ mocha`，就过了。这就是传说中的测试驱动开发：先把要达到的目的都描述清楚，然后让现有的程序跑不过 case，再修补程序，让 case 通过。

安装一个 istanbul : `$ npm i istanbul -g`

执行 `$ istanbul cover _mocha`

这会比直接使用 mocha 多一行覆盖率的输出，

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson6/3.png)

可以看到，我们其中的分支覆盖率是 91.67%，行覆盖率是 87.5%。

打开 `open coverage/lcov-report/index.html` 看看

![](https://raw.githubusercontent.com/alsotang/node-lessons/master/lesson6/4.png)

其实这覆盖率是 100% 的，24 25 两行没法测。

mocha 和 istanbul 的结合是相当无缝的，只要 mocha 跑得动，那么 istanbul 就接得进来。

到此这门课其实就完了，剩下要说的内容，都是些比较细节的。比较懒的同学可以踩坑了之后再回来看。

上面的课程，不完美的地方就在于 mocha 和 istanbul 版本依赖的问题，但为了不引入不必要的复杂性，所以上面就没提到这点了。

假设你有一个项目A，用到了 mocha 的 version 3，其他人有个项目B，用到了 mocha 的 version 10，那么如果你 `npm i mocha -g` 装的是 version 3 的话，你用 `$ mocha` 是不兼容B项目的。因为 mocha 版本改变之后，很可能语法也变了，对吧。

这时，跑测试用例的正确方法，应该是

1. `$ npm i mocha --save-dev`，装个 mocha 到项目目录中去
2. `$ ./node_modules/.bin/mocha`，用刚才安装的这个特定版本的 mocha，来跑项目的测试代码。

`./node_modules/.bin` 这个目录下放着我们所有依赖自带的那些可执行文件。

每次输入这个很麻烦对吧？所以我们要引入 Makefile，让 Makefile 帮我们记住复杂的配置。

```
test:
  ./node_modules/.bin/mocha

cov test-cov:
  ./node_modules/.bin/istanbul cover _mocha

.PHONY: test cov test-cov
```

这时，我们只需要调用 `make test` 或者 `make cov`，就可以跑我们相应的测试了。

至于 Makefile 怎么写？以及 .PHONY 是什么意思，请看这里：http://blog.csdn.net/haoel/article/details/2886 ，左耳朵耗子陈皓2004年的文章。








