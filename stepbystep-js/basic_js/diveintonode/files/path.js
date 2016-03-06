/**
 * Created by patrick on 15/9/5.
 */

var path=require('path');
var cache = {};
function store(key, value) {
    cache[path.normalize(key)] = value;
}

store('foo/bar',1);
store('foo//baz//../bar',2);
console.log(cache);

var extname=path.extname('foo/bar.js');
console.log(extname);

var full_path=path.join('foo/','baz/','../bar');
console.log(full_path);