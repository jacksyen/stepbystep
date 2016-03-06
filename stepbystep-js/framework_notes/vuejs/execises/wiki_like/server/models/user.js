/**
 * Created by patrick on 15/11/15.
 */
'use strict';

var mongoose = require('mongoose'),
    Schema = mongoose.Schema;

var UserSchema = new Schema({
    userNickName: {
        type: Number
    },
    username: {
        type: String,
        default: '',
        trim: true
    }
});

mongoose.model('User', UserSchema);
