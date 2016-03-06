/**
 * Created by patrick on 15/10/23.
 */

var express= require('express');
var app = express();

app.get('/',function(req,res){
   res.end('Hello world!');
});

app.use(express.static('public'));

app.listen(9000,function(){
   console.log("express server is started at 9000");
});