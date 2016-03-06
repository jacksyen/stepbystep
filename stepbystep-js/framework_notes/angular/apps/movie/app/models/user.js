/**
 * Created by patrick on 15/8/9.
 */
var mongoose = require('mongoose')
var UserSchema = require('../schemas/user')
var User = mongoose.model('User', UserSchema)

module.exports = User
