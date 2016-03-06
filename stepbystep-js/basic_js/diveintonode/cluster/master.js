/**
 * Created by patrick on 15/12/27.
 */
var fork = require('child_process').fork;
var cpus = require('os').cpus();
console.log(__dirname);
console.log(cpus.length);
for (var i = 0; i < cpus.length; i++) {
    fork(__dirname + '/worker.js');
}
