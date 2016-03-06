/**
 * Created by patrick on 15/3/4.
 */

fs.readFile('foo.txt','utf-8',function(err,data){
   console.log(data);
});

fs.readFile('bar.txt','utf-8',function(err,data){
   console.log(data);
});

server.on('request',function(req,res){
   memcahed.getSession(req,function(session){
       db.get(session.user,function(userData){
          ws.get(session.user,function(userData){
              page.pageRender(req,session,userData,wsData);
              res.write(page);
          });
       });
   });
});

//refactor
server.on('request',function(req,res){
    var render = function(wsData){
        page = pageRender(req,session,userData,wsData);
    };

    var getWsInfo = function(userData){
        ws.get(req,render);
    };

    var getDbInfo = function(session){
        db.get(req,render);
    };

    var getMemCached = function(req,res){
        memcached.getSession(req,getDbInfo);
    };
});
