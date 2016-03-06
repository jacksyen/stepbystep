/**
 * Created by patrick on 15/10/23.
 */
var page = require('webpage').create()
var system = require('system');
var address =system.args[1];


page.open(address,function(){
    console.log(page.content);
});

//https://github.com/pkainulainen?tab=repositories

//get cookie:

