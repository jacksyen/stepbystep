/**
 * Created by patrick on 15/7/18.
 */
var adminProjects = angular.module('admin-projects',[])
adminProjects.config(function(){
  console.log("start configuration1");
}).config(function(){
  console.log("start configuration2");
}).
  controller('ProjectListCtrl',function($scope){
  console.info("project list logging")
})
.controller('ProjectEditCtrl',function($scope,$log){
    console.info("project edit logging")
  });
