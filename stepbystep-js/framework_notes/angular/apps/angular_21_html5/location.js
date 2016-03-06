/**
 * Created by patrick on 15/7/22.
 */
angular.module('location',[],function($locationProvider){
  $locationProvider.html5Mode(true);
}).controller('MainCtrl',function($scope,$location){
  console.log($location)
  $scope.location=$location;
});
