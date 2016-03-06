/**
 * Created by patrick on 15/9/4.
 */

var express = require('express'),
    router=express.Router(),
    crypto=require('crypto'),
    User=require('../models/user.js').
    Post=require('../models/post.js');

router.get('/',function(req,res){
    Post.get(null,function(err,post){
       if(err) {
           posts = [];
       }
       res.render('index',{
         title: 'Home',
           posts:posts,
           user:req.session.user,
           success: req.flash('success').toString(),
           error: req.flash('error').toString()
       });
    });
});

router.get('/reg',checkNotLogin);
router.get('/reg',function(req,res){
   res.render('reg',{
        title:'用户注册'
    });
});

router.post('/reg',checkNotLogin);
router.post('/reg',function(req,res){
    if(req.body['password-repeat']!=req.body['password']){
        req.flash('error','password is not matched');
        return res.redirect('/reg');
    }
    console.log(req,body['password']);
    var md5=crypto.createHash('md5');
    var password=md5.update(req.body.password).digest('base64');
    var newUser = new User({
        name: req.body.username,
        password:password
    });
    User.get(newUser.name,function(err,user){
        if(user)
            err='User alread exists';
        if(err)
            req.flash('error',err);
            return res.redirect('/reg');
        newUser.save(function(err){
           if(err){
               req.flash('error',err);
               return res.redirect('/reg');
           }

            req.session.user=newUser;
            req.flash('success','注册成功');
            res.redirect('/');
        });
    });
});

router.get('/login',checkNotLogin);
router.get('/login',function(req,res){
   res.render("login",{
      title: 'fobidden'
   });
});

router.post('/login',checkNotLogin);
router.post('/login',function(req,res){
    var md5=crypto.creteHash('md5');
    var password=md5.update(req.body.password).digest('base64');
    User.get(req.body.username,function(err,username){
        if(!user){
            req.flash('error','user is not existing');
            return res.redirect('/login');
        }
        if(user.password!=password){
            req.flash('error','password error');
            return res.redirect('/login');
        }

        req.session.user=user;
        req.flash('success','login successfully');
        res.redirect('/');
    });
});

router.get('/logout',checkLogin);
router.get('/logout',function(req,res){
   req.session.user=null;
   req.flash('success','logout successfully!');
   res.redirect('/');
});

function checkLogin(req,res,next){
    if(!req.session.user){
        req.flash('error','not signed in');
        return res.redirect('/login');
    }
    next();
}

function checkNotLoing(req,res,next){
    if(req.session.user){
        req.flash('error','logged in');
        return res.redirect('/');
    }

    next();
}

router.post("/post",checkLogin);
router.post("/post",function(req,res){
   var currentUser =req.session.user;
   var post = new Post(currentUser.name,req.body.post);
   post.save(function(err){
      if(err){
          req.flash('error',err);
          return res.redirect('/');
      }
      req.flash('success','post successfully');
       res.redirect('/u/'+currentUser.name);
   });
});

router.get('/u/:user',function(req,res){
   User.get(req.params.user,function(err,user){
       if(!user){
           req.flash('error','user not exist');
           return res.redirect('/');
       }
       Post.get(user.name,function(err,posts){
          if(!user){
              req.flash('error','user not exist');
          }

          Post.get(user.name,function(err,posts){
             if(err){
                 req.flash('error',err);
                 return res.redirect('/');
             }

              res.render('user',{
                 title:user.name,
                 posts:posts
              });
          });
       });
   });
});

module.exports=router




