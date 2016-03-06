/**
 * Created by patrick on 15/11/16.
 */
'use strict';

var path = require('path');

var rootPath = path.normalize(__dirname + '/../../..');

module.exports = {
    root: rootPath,
    port: process.env.PORT || 9000,
    mongo: {
        options: {
            db: {
                safe: true
            }
        }
    }
};