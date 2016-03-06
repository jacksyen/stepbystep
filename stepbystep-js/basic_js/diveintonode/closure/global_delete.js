/**
 * Created by patrick on 15/12/27.
 */
global.foo='I am global object';
console.log(global.foo);
delete global.foo;

global.foo=undefined;
console.log(global.foo);

