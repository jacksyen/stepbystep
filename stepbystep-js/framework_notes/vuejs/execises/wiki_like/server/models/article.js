/**
 * Created by patrick on 15/11/15.
 */
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var ArticleSchema = new Schema({
    title:{
        type: String,
        default: '',
        trim:true
    },
    body:{
        type:String,
        default:'',
        trim:true
    },
    html: {
        type: String,
        default: '',
        trim: true
    },
    createdBy: {
        type: Schema.Types.ObjectId,
        ref: 'User'
    },
    updatedBy: {
        type: Schema.Types.ObjectId,
        ref: 'User'
    },
    tags: {
        type: []
    },
    comments: [{
        body: {
            type: String,
            default: ''
        },
        commentedBy: {
            type: Schema.Types.ObjectId,
            ref: 'User'
        },
        createdAt: {
            type: Date,
            default: Date.now
        },
        lastUpdateAt: {
            type: Date,
            default: Date.now
        }
    }],
    category: {
        type: String,
        default: '',
        trim: true
    },
    status: {
        type: Number,
        trim: true,
        default: 1
    },
    createdAt: {
        type: Date,
        default: Date.now
    },
    lastUpdateAt: {
        type: Date,
        default: Date.now
    },
    attr: {
        type: Number,
        default: 0,
        trim: true
    }
    //good or bad
});

ArticleSchema.methods={
  load: function(id,cb){
      this.findOne({_id:id})
          .populate('user')
  }
};