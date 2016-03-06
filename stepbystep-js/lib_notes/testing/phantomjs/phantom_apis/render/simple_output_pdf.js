/**
 * Created by patrick on 15/10/24.
 */

var page = require('webpage').create();
var url = 'http://www.linuxprocess.com/';
t = Date.now();
page.open(url, function (status) {
    console.log("Status:" + status);
    if (status !== 'success') {
        console.log('FAIL to load the address');
    } else {
        t = Date.now() - t;
        console.log('Loading ' + url);
        console.log('Loading time ' + t + ' msec');
        page.render('baidu.pdf');  //capture the screenshot
    }

    phantom.exit();
});