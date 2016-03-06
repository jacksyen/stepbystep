/**
 * Created by patrick on 15/3/4.
 */

EE = require('events').EventEmitter;
ee = new EE();

die = false;
ee.on('die',function(){
   die=true;
});

setTimeout(function(){
   ee.emit('die');
},100);

while(!die){
    console.log('commit');
    ee.emit('die')
}

console.log('done');