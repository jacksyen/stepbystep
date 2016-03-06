angular.module('notificationsApp', []).constant('MAX_LEN',10)
  .controller('NotificationsCtrl', function ($scope, notificationsService) {

    $scope.addNotification = function () {
      notificationsService.push($scope.notification);
      $scope.notification = '';
    };

    $scope.getNotifications = function () {
      return notificationsService.getCurrent();
    };

  })
  .factory('notificationsService', function (notificationsArchive) {
    var notifications = [];

    return {
      push:function (notification) {
        var notificationToArchive;
        var newLen = notifications.unshift(notification);
        if (newLen > config.MAX_LEN) {
          notificationToArchive = this.notifications.pop();
          notificationsArchive.archive(notificationToArchive);
        }
      },
      getCurrent:function () {
        return notifications;
      }
    };
  })
  .factory('notificationsArchive', function () {

    var archivedNotifications = [];
    return {
      archive:function (notification) {
        archivedNotifications.push(notification);
      },
      getArchived:function () {
        return archivedNotifications;
      }};
  });


angular.module('upTimeApp',[]).run(function($rootScope){
  $rootScope.appStart=new Date();
});
