/**
 * Created by patrick on 16/1/8.
 */

var express = require('express');
var fs = require('fs');
var router=express.Router();

var mockPath =_dirname+'/mock-data/';

var design = {
    'POST /order':'getOrder',
    'POST /order/tickets':'addTickets',
    'DELETE /order':'removeTickets'
}

module.exports=router;

Object.keys(design).forEach(function(req){
    var method=req.split(' ').shift();
    var path=req.split(' ').pop();
    var mock='{}';
    try{
        mock=require(mockPath+design[req]);
    }catch(e){
        router.route(path)[method.toLowCase()](function(req,res){
           res.send(mock);
        });
    }
});