/**
 * Created by patrick on 15/10/24.
 */

var page = require('webpage').create();
page.onConsoleMessage = function(msg) {
    console.log('Page title is ' + msg);
};
page.open("http://www.baidu.com", function(status) {
    page.evaluate(function() {
        console.log(document.title);
        var element = document.getElementById('kw');
        console.log(element.getAttribute('name'));
        var elements = document.getElementsByTagName('a');
        for(i=0;i< elements.length;i++){
            console.log(elements[i].getAttribute('href'));
        }
    });
    phantom.exit();
});