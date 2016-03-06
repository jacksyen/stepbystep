/**
 * Created by patrick on 15/8/9.
 */
var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var ObjectId=Schema.Types.ObjectId;

var CommentSchema = new Schema({
  movies: {type:ObjectId,ref:'Movie'},
  from:{type:ObjectId,ref:'User'},
  replay:[{
    from:{type:ObjectId,ref:'User'},
    to:{type:ObjectId,ref:"User"},
    content: String
  }],
  content: String,
  meta:{
    createdAt:{
      type:Date,
      default: Date.now()
    },
    updateAt:{
      type:Date,
      default:Date.now()
    }
  }
});

CommentSchema.pre('save',function(next){
  if (this.isNew) {
    this.meta.createAt = this.meta.updateAt = Date.now()
  }
  else {
    this.meta.updateAt = Date.now()
  }

  next()
});

CommentSchema.statics={
  fetch: function(cb){
    return this.find({}).sort('meta.updateAt').exec(cb);
  },
  findById:function(id,cb){
    return this.findOne({_id:id});
  }
}

module.exports=CommentSchema
