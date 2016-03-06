/**
 * Created by patrick on 15/7/16.
 */
var umService=angular.module('UserManager',['ngRoute']);

function umRouteConfig($routeProvider){
  $routeProvider
    .when('/',{
      controller:listController,
      templateUrl:'list.html'
    })
    .when('/update/:id/:age',{
      controller:updateController,
      templateUrl:'detail.html'
    })
    .when('/delete',{})
    .otherwise({
      redirectTo:'/'
    })
}

umService.config(umRouteConfig);

function listController($scope,$http){
  $http.get('user.json').success(function( data, status, headers, config){
      console.log(data);
    $scope.users=data;
  });
}

function updateController($scope,$http,$routeParams){
  var id = $routeParams.id;
  $http.get('user.json').success(function(data, status, headers, config){
    $scope.xiuUser=getObjectById(id,data);
  });

  $scope.update=function(){
    $http.get('user.json',{params:$scope.xiuUser});
  }
}

function getObjectById(id,obj){
  var len=obj.length;
  for(var i=0;i<len;i++){
    if(id==obj[i].id){
      return obj[i];
    }
  }
  return null;
}
