/**
 * Created by patrick on 15/9/2.
 */

for(var i =0;i<10;i++){
    console.log(i);
}


var TEST_DATA = ['java', 'c#', 'testing', 'ruby',
    'python', 'java web', 'express'];

function select(keyword) {
    var ret = [];
    if (keyword) {
        keyword = keyword.toLowerCase();
        TEST_DATA.forEach(function(element,index){
           console.log(element);
           if(element.toLowerCase().indexOf(keyword)>=0){
               ret.push(element);
           }
        });
    }

    return ret;
}

console.log(select('java web t'));

// for in
for (var element in TEST_DATA){
    console.log(element);
    console.log(TEST_DATA[element])
}

for(var i=0;i<TEST_DATA.length;i++){
    console.log(TEST_DATA[i]);
}

var a_object = {"first":[1,2,3],"second":2,"third":3};
console.log(a_object['second'])
console.log(a_object.second)
for(var element in a_object.second){
    console.log(element);
}

for(var element in a_object){
    console.log(element);
    console.log(a_object[element])
}

console.log(a_object.propertyIsEnumerable("first"));
console.log(a_object.propertyIsEnumerable("second"));