/**
 * Created by patrick on 15/7/19.
 */
angular.module('eventHandles',[])
  .controller('eventHandleCtrl',function($scope){
    $scope.items=['foo','boo','baz'];
    $scope.readPosition =function(item,$event){
      console.log(item + 'was clicked at '+$event.clientX+":"+$event.clientY);
    }
  })
