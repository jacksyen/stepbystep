/**
 * Created by patrick on 15/7/19.
 */
angular.module('jsonp', [])
  .controller('JSONPCtrl', function ($scope, $http) {

    $scope.jsonpGreet = function () {

      $http
        .jsonp('http://angularjs.org/greet.php?callback=JSON_CALLBACK', {
          params:{
            name:'World'
          }
        })
        .success(function (data) {
          $scope.greeting = data;
        }).error(function(data, status, headers, config){
          $scope.greeting="hello errors";
          throw new Error('Something went wrong...'+status);
        });

    };
  });
