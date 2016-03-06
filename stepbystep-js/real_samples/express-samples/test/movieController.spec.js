describe('MovieController',function(){
    //Before each test we tell Angular to load the phonecatApp module.
    beforeEach(module('movieApp'));
    //We ask Angular to inject the $controller service into our test function
    it('should create "movies',inject(function($controller){
        //We use $controller to create an instance of the PhoneListCtrl
        var scope={},
            ctrl=$controller('MovieController',{$scope:scope});
        expect(scope.movies.length).isGreaterThanTen(1);
    }));
})