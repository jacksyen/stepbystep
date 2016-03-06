/**
 * Created by patrick on 15/12/27.
 */
var http = require('http');
var helloworld = "";

for (var i = 0; i < 1024 * 10; i++) {
    helloworld += "a";
}

helloworld = new Buffer(helloworld);

http.createServer(function (req, res) {
    res.writeHead(200);
    res.end(helloworld);
}).listen(1337,function(){
    console.log('server is running,pid:'+process.pid);
});
