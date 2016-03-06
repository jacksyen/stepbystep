/**
 * Created by patrick on 15/10/23.
 */

var http =require('http');

var requestHandle = function(req,res){
    console.log(req);
    res.write(req);
    res.end('hello world');
};

var app=http.createServer(requestHandle);

app.listen(9000, function (){
    console.log("server is listened at 9000");
})
