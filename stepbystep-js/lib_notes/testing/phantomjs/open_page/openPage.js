/**
 * Created by patrick on 15/10/23.
 */
//create HTTP SERVER

var page = require('webpage').create(),
    system=require('system'),
    address;

if(system.args.length==1){
    console.log("exit phantom");
    phantom.exit()
}else{
    address = system.args[1]
    page.open(address,function(status){
        console.log(page.content);
        console.log("exit phantom");
        phantom.exit()
    });
}
