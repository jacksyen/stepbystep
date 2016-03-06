/**
 * Created by patrick on 15/10/23.
 */

// basic concept
// ansync/sync
//callback: 传递
function waitFive(name,function_name){
    var pus=0;
    var currentDate=new Date();
    //while(pus<5000){
    //    var now = new Date();
    //    pus=now-currentDate;
    //}

    function_name(name);
}

function echo(name){
    console.log(name);
}

waitFive('patrick',echo);
console.log("good")

//callback
var test = function(name,callback){
    callback();
    console.log("call back");

};

var test1=function(){
    console.log("this is test");
};

test("patrick",test1);


function Person(){
    this.think = function(callback){
        setTimeout(function(){
            console.log("this is setTimeout callback");
            callback()
        },5000);
    }

    this.answer=function(){
        console.log('I am answering questions');
    }
}

var person = new Person();
person.think(function(){ //callback
   console.log('think 5 seconds,get things done');
});

person.answer()// async: return first, then think function,then callback function

