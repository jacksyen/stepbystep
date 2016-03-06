/**
 * Created by patrick on 15/7/10.
 */

var helloApp  = angular.module('hello',[])
helloApp.controller('helloCtrl',function($scope){
    $scope.name="world";
  })
.controller('worldCtrl',function($scope){
  $scope.population =70000;
  $scope.countries =[
    {name:'FR',population:63.1},
    {name:'UK',population:61.8},
  ]

  $scope.worldsPercentage=function(countryPopulation){
    return (countryPopulation/$scope.population)*100
  }
});
