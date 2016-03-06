/**
 * Created by patrick on 15/7/18.
 */
angular.module('archive',[])
.factory('notificationsArchive',function($scope){
  var archivedNotifications=[];
  return {
    archive:function(notification){
      archivedNotifications.push(notification);
    },
    getArchived:function(){
      return archivedNotifications;
    }
  } ;
})
