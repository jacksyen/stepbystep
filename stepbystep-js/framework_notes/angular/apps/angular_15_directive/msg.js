/**
 * Created by patrick on 15/7/19.
 */
angular.module('expressionsEscaping', ['ngSanitize'])
  .controller('ExpressionsEscapingCtrl', function ($scope) {
    $scope.msg = 'Hello, <b>World</b>!';
  });
