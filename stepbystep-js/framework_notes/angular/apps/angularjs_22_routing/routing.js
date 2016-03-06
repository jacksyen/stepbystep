/**
 * Created by patrick on 15/7/22.
 */
angular.module('routing', ['ngRoute'])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/admin/users/list', {templateUrl: 'users/list.html'})
      .when('/admin/users/new', {templateUrl: 'users/new.html'})
      .when('/admin/users/edit', {templateUrl: 'users/edit.html'})
      .otherwise({redirectTo: '/admin/users/list'});
  })
  .factory('users', function () {
    var users = [
      {id: 1, name: 'next'},
      {id: 2, name: 'other'}];
    return {
      query: function () {
        return users
      },
      add: function (user) {
        users.push(user);
      },
      get: function (id) {
        return users[id];
      },
      update: function (id, user) {
        users[id] = user;
      }
    };
  })
  .controller('NavigationCtrl',function($scope,$location){

  })
.controller('ListUserCtrl',function($scope,users){
    $scope.users = users.query()
  })
.controller('NewUserCtrl',function($scope,users,user){
    users.push(user)
  })
.controller('EditUserCtrl',function($scope,$routParams,users){
    $scope.user=users.get({id:$routParams.id});
  })
