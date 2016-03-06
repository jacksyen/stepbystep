/**
 * Created by patrick on 15/12/27.
 */

process.on('message',function(m,server){
    console.log('start handle message.....');
   if(m==='server'){
       server.on('connection',function(socket){
           socket.end('handled by child\n'+process.pid);
       });
   }
});