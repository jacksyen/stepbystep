/**
 * Created by patrick on 16/1/8.
 */
var json2html = require('./index.js');

describe('json2html(object)', function () {
    it('should return html', function () {
        var html = json2html({'hello': 'world'});
        html.should.equal('{\n\
 <span class="string">"hello"</span>: <span class="string">"world"</span>\n\
}');
    });
});
