/**
 * Created by patrick on 15/9/2.
 */
var adult = {age:26},
    child = Object.create(adult);
child.age = 8;

delete child.age;
/* Remove age property from child, revealing the age of the prototype, because then it is not overriden. */
var prototypeAge = child.age;
console.log(prototypeAge)
// 26, because child does not have its own age property.