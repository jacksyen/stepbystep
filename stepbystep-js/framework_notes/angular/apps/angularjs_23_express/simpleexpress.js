/**
 * Created by patrick on 15/7/22.
 */

var http = require('http');
var express = require('express');
var protectJSON = require('./protectJSON');
var xsrf= require('./xsrf');

var app = express();
var server = http.createServer(app);

app.use(protectJSON);
app.use(xsrf);
//server.use(protectJSON);
//server.use(xsrf);

// Start up the server on the port specified in the config
server.listen(5678);
console.log('Angular App Server - listening on port: 5678');

