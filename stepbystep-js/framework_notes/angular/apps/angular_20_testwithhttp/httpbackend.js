/**
 * Created by patrick on 15/7/21.
 */
angular.module('test-with-http-backend', [])

  .controller('UsersCtrl', function ($scope, $http) {

    $scope.queryUsers = function () {

      $http.get('http://localhost:3000/databases/ascrum/collections/users')
        .success(function (data, status, headers, config) {
          $scope.users = data;
        }).error(function (data, status, headers, config) {
          throw new Error('Something went wrong...');
        });
    };
  });
