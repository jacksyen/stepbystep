/**
 * Created by patrick on 16/2/4.
 */

var data ={data:1};
var vm =new Vue({
   data:data
});

vm.$set('b',2);
//assign some object properties to object
this.someObject = Object.assign({}, this.someObject, { a: 1, b: 2 })
