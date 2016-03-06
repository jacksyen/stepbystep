/**
 * Created by patrick on 15/3/4.
 */
var http = require('http');
http.createServer(function (req, res) {
    res.writeHead(200, {'content-type': 'text/plain'});
    res.end("Hello World!");
}).listen(8124, '127.0.0.1');

console.log('Server Running at http://localhost:8124/');