/**
 * Created by patrick on 15/10/23.
 */
function testFunc1(){
    console.log("this is test");
}

function testFunc2(){
    console.log("this is test2")
}

console.log("this is function result:"+ eval("testFunc2"+"()"));
eval("testFunc2()")
eval("testFunc1()")