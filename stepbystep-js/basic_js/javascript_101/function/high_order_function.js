/**
 * Created by patrick on 15/9/2.
 Higher order functions are functions that manipulate other functions.
 For example, a function can take other functions as arguments and/or produce
 a function as its return value. Such fancy functional techniques are powerful
 constructs available to you in JavaScript and other high-level languages l
 ike python, lisp, etc.
 */


var add_2 = function(x){
 return x+2;
};

var double=function(x){
 return x*2;
};

var map =function(list,func){
 var output=[];
 for(var idx in list){
  console.log(idx); //it is index
  output.push(func(list[idx]))
 }
 return output;
};

console.log(map([5,6,7],add_2));
console.log(map([5,6,7],double));

//build processor
var buildProcessor = function(func){
 var process_func= function(list){
  return map(list,func);
 };
 return process_func;
};

console.log(buildProcessor(add_2));
console.log(buildProcessor(add_2)([5,6,7]));
