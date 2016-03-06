/**
 * Created by patrick on 15/3/4.
 */

var utils = require('utils'),
    EventEmitter = require('events').EventEmitter;
var server = function(){
    console.log('init');
};

//add EventEmitter class to Server class
utils.inherits(Server,EventEmitter);

var s = new Server();

//bundle EventEmitter methods to Server class
s.on('abc',function(){
   console.log('abc');
});

s.emit('abc');