/**
 * Created by patrick on 15/8/30.
 */

var numers =[1,2,3,4,5,6,7,8]

var test ={
    logs:["test"]
}

console.log(test.logs.length)
function length(data,indicator){
    if(!data.hasOwnProperty(indicator)){
        return 0;
    }else{
        return data[indicator].length
    }
}
console.log(length(test,"logs"));
console.log(length(test,"log"));
console.log(test["tst"]);

var data = {
    asset_attributes: [
        {"name":"运维1"},
        {"name":"运维2"},
        {"name":"运维3"},
        {"name":"运维4"},
        {"name":"运维5"}
    ],
        assets_info: [
        {"运维1":"运维","运维2":"运维2","运维3":"运维3","运维4":"运维4","运维5":"运维5"},
        {"运维1":"运维","运维2":"运维2","运维3":"运维3","运维4":"运维4","运维5":"运维5"},
        {"运维1":"运维","运维2":"运维2","运维3":"运维3","运维4":"运维4","运维5":"运维5"},
        {"运维1":"运维","运维2":"运维2","运维3":"运维3","运维4":"运维4","运维5":"运维5"},
        {"运维1":"运维","运维2":"运维2","运维3":"运维3","运维4":"运维4","运维5":"运维5"},
        {"运维1":"运维","运维2":"运维2","运维3":"运维3","运维4":"运维4","运维5":"运维5"}
    ]
};

console.log(data.assets_info[0]["运维1"]);

function get_value(asset_info,key){
    return asset_info[key];
}
console.log('\n');
console.log(get_value(data.assets_info[0],"运维1"));