/**
 * Created by patrick on 15/3/4.
 */
var http=require('http');

var opts ={
    host: 'localhost',
    port: 9001,
    path:'/'
};

var req = http.get(opts,function(res){
   console.log("this will never be called");
});

req.on('error',function(e){
   console.log('Got that error!!');
});