/**
 * Created by patrick on 15/12/27.
 */
var net = require('net');

var server = net.createServer(function (socket) {
    socket.write('Echo server\r\n');
    socket.pipe(socket);
});

server.listen(1337, '127.0.0.1');
