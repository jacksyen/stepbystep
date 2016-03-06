/**
 * Created by patrick on 15/12/27.
 */
// child.js
var http = require('http');
//create server
var server = http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('handled by child, pid is ' + process.pid + '\n');
});

var worker;
process.on('message', function (m, tcp) {
    if (m === 'server') {
        worker = tcp;
        worker.on('connection', function (socket) {
            server.emit('connection', socket);
        });
    }
});

process.on('uncaughtException', function (err) {
    process.send({act: 'suicide'});
    worker.close(function () {
        process.exit(1);
    });
});
