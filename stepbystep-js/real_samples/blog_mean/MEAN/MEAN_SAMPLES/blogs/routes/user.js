/**
 * Created by patrick on 15/9/4.
 */

var express =require('express');
var router=express.Router();

router.get('/',function(req,res){
   res.send('response with a resources');
});

module.exports=router;