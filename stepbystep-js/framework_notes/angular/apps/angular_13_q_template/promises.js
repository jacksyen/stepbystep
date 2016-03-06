/**
 * Created by patrick on 15/7/19.
 */
angular.module('promises',[])
.controller('PromiseCtrl',function($scope,$timeout){
    $scope.name=$timeout(function(){
      return "World";
    },200);

    $scope.getName=function(){//callback hell
      return $timeout(function(){
        console.log("start return in getName")
        return "World";
      });
    };

    $timeout(function(){
      console.log("start return in timeout function")
      return "World";
    },200).then(function(value){
      console.log("start return in then")
      $scope.name=value;
    });
  });
