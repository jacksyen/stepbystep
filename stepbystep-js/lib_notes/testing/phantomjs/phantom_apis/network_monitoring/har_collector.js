/**
 * Created by patrick on 15/10/24.
 */

var page = require('webpage').create();
var url="http:www.baidu.com";

page.onResourceRequested = function(request) {
    console.log('Request ' + JSON.stringify(request, undefined, 4));
};
page.onResourceReceived = function(response) {
    console.log('Receive ' + JSON.stringify(response, undefined, 4));
};
page.open(url);