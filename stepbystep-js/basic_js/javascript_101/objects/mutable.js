/**
 * Created by patrick on 15/9/2.
 */
var myPrimitive = "first value";
myPrimitive = "another value";
console.log(myPrimitive);
// myPrimitive now points to another string.
var myObject = { key: "first value"};
myObject.key = "another value";
console.log(myObject);
// myObject points to the same object.