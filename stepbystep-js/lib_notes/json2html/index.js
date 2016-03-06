'use strict';

module.exports = json2html;

/**
 * escape given string of 'html'
 * @param html
 */
function escape(html){

    return String(html)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
}

/**
 * return a span html section
 * @param className
 * @param str
 * @returns {string}
 */
function span(className,str){
    return '<span class="'+className+'">'+str+'</span>';
}

/**
 * convert json object to HTML
 * @param obj
 * @param indents
 */
function json2html(obj,indents){
    var indents = indents ||1;

    function indent(){
        return Array(indents).join(' ');
    }

    if('string'== typeof  obj){
        return span('string value', '"' + escape(obj) + '"');
    }

    if('number' == typeof obj){
        return span('number', obj);
    }

    if ('boolean' == typeof obj) {
        return span('boolean', obj);
    }

    if (null === obj) {
        return span('null', 'null');
    }

    if (Array.isArray(obj)) {
        ++indents;

        var buf = '[\n' + obj.map(function(val){
                return indent() + json2html(val, indents);
            }).join(',\n');

        --indents;
        buf += '\n' + indent() + ']';
        return buf;
    }

    var buf = '{';
    var keys = Object.keys(obj);
    var len = keys.length;
    if (len) buf += '\n';

    ++indents;
    buf += keys.map(function(key){
        var val = obj[key];
        key = '"' + key + '"';
        key = span('string key', key);
        return indent() + key + ': ' + json2html(val, indents);
    }).join(',\n');
    --indents;

    if (len) buf += '\n' + indent();
    buf += '}';

    return buf;
}