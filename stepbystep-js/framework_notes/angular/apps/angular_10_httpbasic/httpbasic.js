/**
 * Created by patrick on 15/7/19.
 */
angular.module('basic', [])
  .controller('basicCtrl', function ($scope, $http) {
    $scope.name = function () {
      var futureResponse = $http.get('user.json');
      futureResponse.success(function (data, status, headers, config) {
        $scope.data = data;
      });

      futureResponse.error(function (data, status, headers, config) {
        throw new Error('something went wrong,man,keep calm.........')
      });
    };
    $scope.getNameThen = function () {
      var responsePromise = $http.get('user.json');
      responsePromise.then(function (response) {
        $scope.data = response.data;
      }, function (response) {
        throw new Error('something went wrong ,man, keep calm..........')
      });
    };

    $scope.queryUsers=function(){
      $http.get('user.json').success(function(data,status,headers,config){
        $scope.users= data;
      }).error(function(data,status,headers,config){
        throw new Error('Something is wrong.......')
      });
    };

    $scope.queryUsersG= function(){
      $http.get('user.json').success(function(data,status,headers,config){
        $scope.userG = data;
      }).error(function(data,status,headers,config){
        throw new Error('Something is wrong.......')
      });
    };

    $scope.addUser=function(user) {
      var userAdd ={
        name:'test user'
      };
      $http.post().success(function(data,status,headers,config){
        $scope.newUser=userAdd;
      }).error(function(data,status,headers,config){
        throw new Error("something went wrong.........")
      });
    }; $scope.addUser = function (user) {

      var userToAdd = {
        name:'AngularJS Superhero',
        email:'superhero@angularjs.org'
      };

      $http.post('https://api.mongolab.com/api/1/databases/ascrum/collections/users',
        userToAdd, {
          params:{
            apiKey:'4fb51e55e4b02e56a67b0b66'
          }
        }).success(function (data, status, headers, config) {
          $scope.newUser = data;
        }).error(function (data, status, headers, config) {
          throw new Error('Something went wrong...');
        });
    };

  });
