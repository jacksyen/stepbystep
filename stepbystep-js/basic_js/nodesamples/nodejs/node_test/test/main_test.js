/**
 * Created by patrick on 15/7/28.
 */
var main = require('../main');
var should =require('should');

describe('test/main_test.js',function(){
    it('should equal = when n===0',function(){
        main.fib(0).should.equal(0);
    })
})