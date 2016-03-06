/**
 * Created by patrick on 15/9/4.
 */
var mongo = require('./db');

function User(user){
    this.name=user.name;
    this.password=user.password;
}

module.exports = User;

User.prototype.save=function save(callback){
    var user={
        name:this.name,
        password: this.password
    };

    mongo.open(function(err,db){
       if(err) return callback(err);
       db.collection('users',function(err,collection){
          if(err){
              mongo.close();
              return callback(err);
          }
          collection.insert(user,{saft:true},function(err,user){
             mongo.close();
             callback(err,user);
          });
       });
    });
}

User.get=function get(username,callback){
    mongo.open(function(err,db){
        if(err) return callback(err);
        db.collection('users',function(err,collection){
           if(err){
               mongo.close();
               return callback(err);
           }
            collection.findOne({name:username},function(err,doc){
               if(err){
                   mongo.close();
                   return callback(err);
               }
               if(doc){
                   var user = new User(doc);
                   callback(err,user);
               } else{
                    callback(err,null);
                }

            });
        });
    })
}