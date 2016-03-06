/**
 * Created by patrick on 15/10/16.
 */

var page = require('webpage').create();
page.onResourceRequested = function(request) {
    console.log('Request ' + JSON.stringify(request, undefined, 4));
};
page.onResourceReceived = function(response) {
    console.log('Receive ' + JSON.stringify(response, undefined, 4));
};
page.open("http://www.baidu.com",function(status){
    console.log("Status:"+status);
    if(status==='success'){
        page.render('baidu.png'); //capture the screenshot
    }
    phantom.exit();
});
