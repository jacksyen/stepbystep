/**
 * Created by patrick on 15/12/27.
 */
var fs = require('fs');
var path = require('path');

var rs = fs.createReadStream(path.join(__dirname, 'test.md'), {highWaterMark: 11});
var data = '';
rs.setEncoding('utf8');
rs.on("data", function (trunk) {
    console.log('data');
    data += trunk;
});
rs.on("end", function () {
    console.log(data);
});
