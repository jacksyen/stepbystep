/**
 * Created by patrick on 15/12/27.
 */
var fs = require('fs');

var reader = fs.createReadStream('in.txt');
var writer = fs.createWriteStream('out.txt');
reader.pipe(writer);
