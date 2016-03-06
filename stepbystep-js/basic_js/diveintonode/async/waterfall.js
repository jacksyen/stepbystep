/**
 * Created by patrick on 15/12/27.
 */

var async = require('async');

async.waterfall([
    function(callback){
        console.log(arguments);
        setTimeout(function(){
           callback(null,'one','two');
        },20);
    },
    function(arg1,arg2,callback){
        console.log(arguments);
        setTimeout(function(){
           callback(null,'three');
        },10);
    }],function(err,result){
    console.log(arguments);
});