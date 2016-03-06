/**
 * Created by patrick on 15/9/2.
 */
var myCounter = {
    number : 0,
    plusPlus : function(){
        this.number=this.number + 1;
    },
    isGreaterThanTen : function(){
        return this.number > 10;
    }
}