/**
 * Created by patrick on 15/3/2.
 */

var net = require('net');
var charServer = net.createServer();
clientList =[]

charServer.on('connection',function(client){

    client.name=client.remoteAddress+":"+client.remotePort;
    client.write('Hi '+client.name+"!\n");
    clientList.push(client);

    charServer.on('data',function(data){
        broadcast(data,client);
    });

    function broadcast(message,client){
        for (var i=0;i<clientList.length;i++){
            clientList[i].write(client.name+"says"+data);
        }
    }
});

charServer.listen(9001);

