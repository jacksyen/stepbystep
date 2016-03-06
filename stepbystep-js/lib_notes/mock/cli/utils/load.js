/**
 * Created by patrick on 15/12/18.
 */

var path = require('path');
var got = require('got');
var low = require('lowdb');
var is = require('./is')

module.exports = function (source, cb) {
    var data;
    if (is.URL(source)) {
        got(source, {json: true}, function (err, data) {
            cb(err, data);
        })
    } else if (is.JS(source)) {
        var fileName = path.resolver(source);
        delete require.cache[fileName];
        data = require(fileName);
        cb(null, data);
    } else if (is.JSON(source)) {
        data = low(source).object;
        cb(null, data);
    } else {
        throw new Error('Unsupported source ' + source);
    }
}