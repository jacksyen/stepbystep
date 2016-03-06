/**
 * Created by patrick on 15/10/24.
 */
var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'SpecialAgent';
var url="http://www.httpuseragent.org"
page.open(url, function(status) {
    if (status !== 'success') {
        console.log('Unable to access network');
    } else {
        var ua = page.evaluate(function() {
            return document.getElementById('myagent').textContent;
        });
        console.log(ua);
        phantom.exit();
    }

});