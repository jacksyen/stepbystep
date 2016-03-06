/**
 * Created by patrick on 15/3/4.
 */
var cluster =require('cluster');
var http= require('http');
var numCPUs = require('os').cpus().length;
console.log(numCPUs);

if(cluster.isMaster){
  for (var i =0;i<numCPUs;i++){
      cluster.fork();
  } ;

  cluster.on('death',function(worker){
    console.log('worker'+worker.pid+" died")
  });
}else{
    http.Server(function(req,res){
        res.writeHead(200);
        res.end("hello world");
    }).listen(9000);
};

//status shared
var rssWarn = (12*1024*1024);
var heapWarn=(10*1024*1024);
if(cluster.isMaster){
    for(var i =0;i<numCPUs;i++){
        var worker = cluster.fork();
        worker.on('message',function(m){
           if(m.memory){
              if(m.memory.rss>rssWarn){
                  console.log('Worker '+ m.process+' using too much memory');
              }
           }else{
               http.server(function(req,res){
                  res.writeHead(200);
                  res.end('hello world!');
               }).listen(9000);

               setInterval(function report(){
                   process.send({memory:process.memoryUsage(),
                   process:process.pid});
               },1000);
           } ;
        });
    }
}