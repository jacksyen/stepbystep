movieApp = angular.module('movieApp', ['ngRoute', 'ngResource','MovieControllers']);
movieApp.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'views/home.html',
            controller: 'MovieController'
        })
        .when('/home', {
            templateUrl: 'views/home.html',
            controller: 'MovieController'
        })
        .when('/movie/:id', {
            templateUrl: 'views/movie.html',
            controller: 'MovieDetailsController'
        }).otherwise({
        redirectTo: '/'
    })
}]);