/**
 * Created by patrick on 15/9/2.
 */
function double1(x){
    console.log('this is in function')
    return 2*x;
}

var double = function(x){
    console.log('this is variable')
    return 2*x;
}

console.log(double1(2));
console.log(double(2));