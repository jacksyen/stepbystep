/**
 * Created by patrick on 15/11/15.
 */
'use strict';

var mongoose = require('mongoose'),
    Schema = mongoose.Schema;

/**
 *
 */

var FeedbackSchema = new Schema({
    linkTo: {
        type: String,
        default: ''
    },
    body: {
        type: String,
        default: ''
    },
    user: {
        type: Schema.Types.ObjectId,
        ref: 'User'
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});


mongoose.model('Feedback', FeedbackSchema);
