/**
 * Created by patrick on 15/9/4.
 */

var mongo = require('./db');

function Post(username,post,time){
    this.user=username;
    this.post = post;
    if(time){
        this.time=time;
    }else{
        this.time=new Date();
    }
};

module.exports=Post;

Post.prototype.save = function save(callback){
    var post ={
        user:this.user,
        post:this.post,
        time:this.time
    };

    mongo.open(function(err,db){
       if(err){
           return callback(err);
       }

        db.collection('posts',function(err,collection){
            if(err){
                mongo.close();
                return callback(err);
            }
            collection.insert(post,{safe:true},function(err,post){
                mongo.close();
                callback(err,post);
            });
        })
    });
};

Post.get= function get(username,callback){
    mongo.open(function(err,db){
       if(err) return callback(err);
        db.collection('posts',function(err,collection){
           if(err){
               mongo.close();
               return callback(err);
           }

            var query= {};
            if(username){
                query.user=username;
            }
            collection.find(query).sort({time:-1})
                .toArray(function(err,docs){
                    mongo.close();
                    if(err){
                        callback(err,null);
                    }
                    var posts =[];
                    docs.forEach(function(doc,index){
                        var post = new Post(doc.user,doc.post,doc.time)
                        posts.push(post);
                        callback(null,posts);
                    });
                }
            );
        });
    });
}

