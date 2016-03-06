/**
 * Created by patrick on 15/12/27.
 */

var net=require('net');

var server = net.createServer(function(socket){
   socket.on('data',function(data){
      socket.write("Hello Buddy");
   });

    socket.on('end',function(){
        console.log('client give up');
    });
    socket.write('welcome to the node world!');
});

server.listen(8124,function(){
   console.log('server start......');
});