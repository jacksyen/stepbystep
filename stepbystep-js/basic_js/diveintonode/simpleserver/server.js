/**
 * Created by patrick on 15/12/27.
 */
"use strict";

var http = require('http');
var url = require('url');

var parseCookie = function (cookie) {
    var cookie = {};
    if (!cookie) {
        return cookie;
    }
    var cookieList = cookie.split(';');
    for (var i = 0; i < cookieList.length; i++) {
        var pair = cookieList[i].split('=');
        cookie[pair[0].trim()] = pair[1];
    }
    return cookie;
};

var checkUser = function () {
    return false;
};

http.createServer(function (req, res) {
    console.log(req.method);
    console.log(req);
    console.log(req.url);
    console.log(req.headers);
    res.writeHead(200, {'Content-Type': 'text/plain'});
    //res.end('Hello World \n');
    res.end('<html><body>Hello World</body></html>\n');

}).listen(1337, '127.0.0.1', function () {
    console.log('Server is running at 127.0.0.1:1337')
});
