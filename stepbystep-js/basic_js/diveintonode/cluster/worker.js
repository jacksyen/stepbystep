/**
 * Created by patrick on 15/12/27.
 */

var http = require('http');
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello World\n');
// }).listen(Math.round((1 + Math.random()) * 1000), '127.0.0.1');
}).listen(1337, '127.0.0.1',function(){
    console.log('running at 1337 localhost')
});