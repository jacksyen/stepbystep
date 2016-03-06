/**
 * Created by patrick on 15/7/19.
 */
angular.module('repeaterBasics',[])
  .controller('RepeaterBasicsCtrl',function($scope){
    $scope.users=[
      {name:'simon',email:'1234@domain.com',desc:"description1"},
      {name:'tester',email:'123456@domain.com',desc:"description2"}
    ];
    $scope.user=$scope.users[0];
    $scope.selectUser =function(user){
      $scope.selectedUser=user;
    }

    $scope.isSelected=function(user){
      return $scope.selectedUser === user;
    }
  });
