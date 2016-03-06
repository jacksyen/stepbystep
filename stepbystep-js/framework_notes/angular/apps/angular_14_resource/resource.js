/**
 * Created by patrick on 15/7/19.
 */
angular.module('resource',['ngResource'])
  .factory('Users',function(resource){
    var Users = $resource('user.json');
    Users.prototype.getFullName = function(){
      return this.firstName+':'+this.lastName;
    };
    return Users;
  })
.controller('ResourceCtrl',function(){
    $scope.users = Users.query({},function(users){
      console.log($scope.users.length);
    });

    $scope.remove = function(user,index){
      Users['delete']({},user);
      $scope.users.splice(index,1);
    };

    $scope.add =function(){
      var user = new Users({
        name:'Superhero'
      });
      user.save();
    };

    $scope.add = function () {
      var user = {
        name:'Superhero'
      };
      Users.save(user);
    };

  })
