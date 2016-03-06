/**
 * Created by patrick on 15/3/5.
 */

var http = require('http');
var options ={
    host:"www.baidu.com",
    //port:80,
    path:"/",
    method:"GET"
};

var req = http.request(options,function(res){
    res.setEncoding('utf8');
    res.on('data',function(chunk){
        console.log('BODY:'+chunk);
    });
});

//send data
req.write("my data");
req.write("more of my data");
req.end();

