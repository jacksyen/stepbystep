var movieControllers = angular.module('MovieControllers', ['ngResource']);

movieControllers.controller("MovieController", function ($scope,movieFactory) {
    console.log(movieFactory);
    $scope.contentHeader = "views/partial/content_header.html";
    $scope.movies=movieFactory.query();

    $scope.currMovie = null;
    $scope.getMovieById = function (id) {
        var movies = $scope.movies;
        for (var i = 0; i < movies.length; i++) {
            var movie = $scope.movies[i];
            if (movie.id == id) {
                $scope.currMovie = movie
            }
        }
    };
    $scope.back = function () {
        window.history.back();
    };
    $scope.getCount=function(n){
        return new Array(n);
    }
});
movieControllers.controller(
    "MovieDetailsController", ['$scope', '$routeParams', function ($scope, $routeParams) {
        console.log("get movie to " + $routeParams.id);
        console.log($scope.getMovieById($routeParams.id));
    }]
);