/**
 * Created by patrick on 15/12/27.
 */

process.nextTick(function(){
   console.log('lazy execution');
});

console.log('execution well enough');