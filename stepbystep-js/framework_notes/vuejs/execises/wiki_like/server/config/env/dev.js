/**
 * Created by patrick on 15/11/16.
 */
'use strict';

module.exports = {
    env: 'dev',
    port: process.env.PORT || 9000,
    mongo: {
        uri: 'mongodb://localhost/wikilike'
    }
};