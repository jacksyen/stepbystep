/**
 * Created by patrick on 15/11/16.
 */
'use strict';

module.exports = {
    env: 'production',
    ip:   process.env.IP || '0.0.0.0',
    port: process.env.PORT || 9000,
    mongo: {
        uri: 'mongodb://<server>/wikilike'
    }
};