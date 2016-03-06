/**
 * Created by patrick on 15/3/4.
 */
var http = require('http');
var server = http.createServer();
var handleReq = function(req,res){
  res.writeHead(200,{});
  res.end('hello world!')
};

server.on('request',handleReq());
server.listen(9001);

//http 事件 request,checkContinue,upgrade,clientError
