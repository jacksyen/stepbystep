/**
 * Created by patrick on 15/7/18.
 */
angular.module('app',['engines'])
.controller('appCtrl',function($scope,car){
    car.start()
  })
.factory('car',function($log,dieselEngine){
    return {
      start:function(){
        $log.info('Starting' +dieselEngine.type)
      }
    }
  });

angular.module('engines',[]).factory('dieselEngine',function(){
  return {
    type:'diesel'
  }
});
