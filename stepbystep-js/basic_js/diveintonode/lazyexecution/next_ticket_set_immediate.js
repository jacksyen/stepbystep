/**
 * Created by patrick on 15/12/27.
 */

process.nextTick(function () {
   console.log('next ticket 延迟执行1')
});

process.nextTick(function(){
    console.log('next ticket 延迟执行2')
});

setImmediate(function(){
   console.log('set immediate 延迟执行1');
   process.nextTick(function(){
      console.log('exec 1')
   });
});

setImmediate(function(){
    console.log('exec 2')
});

console.log('execution well');