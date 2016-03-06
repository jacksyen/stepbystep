/**
 * Created by patrick on 15/7/28.
 */
var fib= function(n){
    if (typeof n!=='number'){
        throw new Error('should be a number');
    }

    if(n<0){
        throw new Error('should >=0');
    }

    if(n>10){
        throw new Error('should <=10');
    }

    if(n===0){
        return 0;
    }

    if(n===1){
        return 1;
    }

    return fib(n-1)+fib(n-2);
};

exports.fib=fib;

if (require.main===module){
    var n = Number(process.argv[2]);
    console.log('fib('+n+') is',fib(n))
}