/**
 * Created by patrick on 15/10/24.
 */
var page = require('webpage').create();
var address = phantom.args[0];

console.log(phantom.scriptName);

page.onConsoleMessage = function (msg) {
    console.log('Page title is ' + msg);
};

page.onError=function(msg,trace){
    console.log(msg);
    console.log(trace);
    console.log("page has error");
}

phantom.onError = function (msg, trace) {
    var msgStack = ['PHANTOM ERROR:' + msg];
    if (trace && trace.length) {
        msgStack.push('Trace:');
        trace.forEach(function (t) {
            msgStack.push(' -> ' + (t.file || t.sourceURL) + ': ' + t.line + (t.function ? ' (in function ' + t.function + ')' : ''));
        });
    };
    console.error(msgStack.join('\n'));
    phantom.exit(0);
}

page.open(address, function (status) {
    console.log(phantom.cookies);
    phantom.addCookie({"abcd": "Test"});
    phantom.deleteCookie("adbcd")
    phantom.clearCookies();
    console.log(phantom.cookieEnabled)
    phontom.injectJS("simple.js")
    console.log(phantom.libraryPath)
    page.evaluate(function () {
        console.log(document.title);
    });
});