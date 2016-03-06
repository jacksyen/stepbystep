/**
 * Created by patrick on 15/9/5.
 */
var fs =require('fs');

function copy(src,dest){
    fs.writeFileSync(dest,fs.readFileSync(src));
}

function copyBystream(src,dest){
    fs.createReadStream(src).pipe(fs.createWriteStream(dest));
}

function main(argv){
    copy(argv[0],argv[1]);
}

main(process.argv.slice(2));