/**
 * Created by patrick on 15/12/27.
 */

var fs = require('fs');
var async = require('async');

async.parallel([
    function (callback) {
        fs.readFile('file1.txt', 'utf-8', callback);
    },
    function (callback) {
        fs.readFile('file2.txt', 'utf-8', callback);
    }
], function (err, results) {
    console.log(results);
});