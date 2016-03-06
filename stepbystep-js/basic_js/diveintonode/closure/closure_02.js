/**
 * Created by patrick on 15/12/27.
 */

var foo1 = function () {
    (function () {
        var local = "局部变量";
    }());
    console.log(local);
};

//error
foo1();