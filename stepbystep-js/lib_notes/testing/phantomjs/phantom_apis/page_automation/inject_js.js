/**
 * Created by patrick on 15/10/24.
 */


var page = require('webpage').create();
var url ="http://www.baidu.com";
var cdn_url= 'http://cdn.staticfile.org/jquery/2.1.1-rc2/jquery.min.js';

page.open(url, function() {
    page.injectJs(cdn_url, function() {
        page.evaluate(function() {
            $("#kw").value="test";
            $("button").click();
        });
    });
    page.render('baidu.com')
    phantom.exit()
});