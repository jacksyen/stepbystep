/**
 * Created by patrick on 15/6/21.
 */
function foo(){
    value = "hello";
    var test="test";
}

foo();
console.log(value);
console.log(global.value);
console.log(foo.test);