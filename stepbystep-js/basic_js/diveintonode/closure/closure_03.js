/**
 * Created by patrick on 15/12/27.
 */

var foo = function () {
    var bar = function () {
        var local = "局部变量";
        return function () {
            return local;
        };
    };
    var baz = bar();
    console.log(baz());
};
foo();