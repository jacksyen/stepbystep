/**
 * Created by patrick on 15/9/2.
 */

/**
 * Objects are never copied. They are passed around by reference.
 */


// Imagine I had a pizza
var myPizza = {slices: 5};
// And I shared it with You
var yourPizza = myPizza;
// I eat another slice
myPizza.slices = myPizza.slices - 1;
console.log(myPizza);
console.log(yourPizza);

var numberOfSlicesLeft = yourPizza.slices;
console.log(numberOfSlicesLeft)
// Now We have 4 slices because myPizza and yourPizza
// reference to the same pizza object.
var a = {}, b = {}, c = {};
// a, b, and c each refer to a
// different empty object
a = b = c = {};
// a, b, and c all refer to
// the same empty object
console.log(a===b);
console.log(a===c);