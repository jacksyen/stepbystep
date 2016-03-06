/**
 * Created by patrick on 15/8/8.
 */

try{
    setImmediate(function(){
        throw new Error('error')
    },200);
}catch(err){
    console.log(err)
}

function getJSON(file,callback){
    fs.readFile(file,function(err,content){
        if(err) return callback(err);
        try{
            context=JSON.parse(content);
        }catch(err){
            return callback(err);
        }
        return callback(null,content)
    })
}

getJSON('package.json',function(err,content){
   if(err) console.error(err.stack);
});

//callback hell
getUser(function(err,user){
    if(err) return callback(err);
    getArticle(function(err,artile){
        if (err) return callback(err);
        res='test'
        callback(null,res);
        //......
    });
})