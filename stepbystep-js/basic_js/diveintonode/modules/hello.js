/**
 * Created by patrick on 15/12/27.
 */

var hw = require('./helloworld.js')
function hello(message){
    console.log(message)
    console.log(hw.sayHello());
}



exports.hello =hello;