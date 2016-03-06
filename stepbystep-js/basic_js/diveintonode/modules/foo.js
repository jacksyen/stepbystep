/**
 * Created by patrick on 15/9/4.
 */

function Foo() {
    var name = 'foo';
    var hello =function(message){
        console.log('hello world');
        console.log('hello '+message)
    }

}

module.exports=Foo()