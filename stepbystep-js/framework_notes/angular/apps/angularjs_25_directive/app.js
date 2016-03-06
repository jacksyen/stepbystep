/**
 * Created by patrick on 15/7/22.
 */
var app = angular.module('myApp',[]);
app.controller('selectCtrl',function($scope){
  $scope.myChoice=3;
  $scope.options=[
    {name:'one',value:1},
    {name:'two',value:2},
    {name:'three',value:3},
    {name:'four',value:4}
  ];
}).controller('mainCtrl',function($scope){
  $scope.users = [
    { firstName: 'Jo', lastName: 'Jordan', email: 'jo@jordan.com', sex:"Female"},
    { firstName: 'Anne', lastName: 'Asher', email: 'anne@asher.com', sex:"Female"},
    { firstName: 'Steve', lastName: 'Stone', email: 'steve@stone.com', sex:"Male"},
    { firstName: 'Kev', lastName: 'King', email: 'kev@king.com', sex:"Male"}
  ];

  $scope.getFullName = function(user) {
    return user.firstName + ' ' + user.lastName;
  };

})
