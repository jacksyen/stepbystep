/**
 * Created by patrick on 15/9/5.
 */
var fs=require('fs');
var hello = new Buffer('hello','utf-8');
console.log(hello);
var sub=hello.slice(2);
console.log(sub);
console.log(sub.toString());
var bin = new Buffer([ 0x68, 0x65, 0x6c, 0x6c, 0x6f ]);
var dup = new Buffer(bin.length);
bin.copy(dup);

dup[0]=0x48;
console.log(bin);
console.log(dup);


//stream

var fs = require('fs');
var rs = fs.createReadStream('../files/1.txt');
var ws=fs.createWriteStream('2.txt');

//我们把doSomething换成了往只写数据流里写入数据后，
// 以上代码看起来就像是一个文件拷贝程序了。
// 但是以上代码存在上边提到的问题，如果写入速度跟不上读取速度的话，
// 只写数据流内部的缓存会爆仓。
// 我们可以根据.write方法的返回值来判断传入的数据是写入目标了，
// 还是临时放在了缓存了，
// 并根据drain事件来判断什么时候只写数据流已经将缓存中的数据写入目标，
// 可以传入下一个待写数据了。因此代码可以改造如下：


rs.on('data',function(chunk){
   console.log(chunk.toString());
   //ws.write(chunk.toString());
    if(ws.write(chunk)===false){
        rs.pause();
    }
});

rs.on('end',function(){
    console.log('end of reading');
    ws.end();
});

ws.on('drain',function(){
    rs.resume();
});

//same as pipe functionality

////fs module
//- fs.stat
//- fs.chmod
//-fs.chown
//-fs.readFile()
//-fs.writeFile();
//- fs.readFile、fs.readdir、fs.writeFile、fs.mkdir
//- fs.open、fs.read、fs.write、fs.close

//nodejs- 异步

fs.readFile('5.txt',function(err,data){
    if(err){
        console.log(err);
    }else{
        console.log(data);
    }
});

try {
    var d = fs.readFileSync('5.txt');
}catch(err){
    console.log(err);
}

