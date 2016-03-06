/**
 * Created by patrick on 15/11/16.
 */
'use strict';

var _ = require('lodash');

/**
 * Load environment configuration
 */
module.exports = _.merge(
    require('./env/all.js'),
    require('./env/' + process.env.WIKI_ENV + '.js') || {});