/**
 * Created by patrick on 15/7/22.
 */
var fs = require('fs');
var http = require('http');
var https = require('https');
var privateKey = fs.readFileSync('cert/privatekey.gem').toString();
var certificate = fs.readFileSync('cert/certificate.pem').toString();
var credentials = {key: privateKey, cert: certificate};

var express = require('express');
var app=express();
var secureServer=https.createServer(credentials,app);
var server = http.createServer(app);

server.listen(5678,function(){
  console.log('Angular App Server - Listening on port:5678');
});
secureServer.listen(95678,function(){
  console.log('Angular App Server - Listening on secure port : 95678');
});

app.listen(4350,function(){
  console.log('express server - listening on port : 4530');
})
