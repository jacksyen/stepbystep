/**
 * Created by patrick on 15/12/27.
 */

var foo = function () {
    var local = 'local variable';
    (function () {
        console.log(local);
    });
};



foo();
