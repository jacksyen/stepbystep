/**
 * Created by patrick on 15/9/2.
 */
var adult = {age: 26},
    retrievedProperty = adult.age;
var stringRepresentation = adult.toString();
adult.toString = function(){
    return "I'm "+this.age;
}


var child = Object.create(adult);
/* This way of creating objects lets us easily replace the default Object.prototype with the one we want. In this case, the child's prototype is the adult object. */
child.age = 8;
/* Previously, child didn't have its own age property, and the interpreter had to look further to the child's prototype to find it.
 Now, when we set the child's own age, the interpreter will not go further.
 Note: adult's age is still 26. */
var stringRepresentation = child.toString();
// The value is "I'm 8".
/* Note: we have not overridden the child's toString property,
thus the adult's method will be invoked.
If adult did not have toString property,
then Object.prototype's toString method would be invoked,
and we would get "[object Object]" instead of "I'm 8" */