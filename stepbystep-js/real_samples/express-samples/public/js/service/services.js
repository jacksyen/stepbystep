/**
 * Created by patrick on 16/3/5.
 */
movieApp.factory('movieFactory',function($resource){
   return $resource('/movies');
});