/**
 * Created by patrick on 15/7/18.
 */
angular.module('upTimeApp',[]).run(function($rootScope){
  $rootScope.appStarted=new Date();
});
