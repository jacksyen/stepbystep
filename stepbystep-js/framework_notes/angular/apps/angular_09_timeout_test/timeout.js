/**
 * Created by patrick on 15/7/18.
 */
angular.module('async',[])
.factory('asyncGreeter',function($timeout,$log){
    return {
      say:function(name,timeout){
       $timeout(function(){
         $log.info("hello,"+name+"!");
       },timeout);
      }
    };
  });
