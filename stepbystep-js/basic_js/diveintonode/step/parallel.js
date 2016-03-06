/**
 * Created by patrick on 15/12/27.
 */
var fs = require('fs');
var Step = require('step');

Step(
    function readFile1() {
        var f1= fs.readFile('file1.txt', 'utf-8', this.parallel());
        console.log(f1)
        var f2 = fs.readFile('file2.txt', 'utf-8', this.parallel());
        console.log(f2)
    },
    function done(err, content1, content2) {
        // content1 => file1
        // content2 => file2
        console.log(arguments);
    }
);
