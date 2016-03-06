/**
 * Created by patrick on 15/3/4.
 */

function a(x,y){
    y= function(){x=2};
    return function(){
        var x =3;
        console.log(x);
    }.apply(this,arguments);
}

a();