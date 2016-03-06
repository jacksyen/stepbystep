/**
 * Created by patrick on 15/8/30.
 */

var country= 'England';
var weather;
var food;
var currency;

if(country==='England'){
    weather='horrible';
    food='filling';
    currency='pound';
}else if(country==='France'){

    weather='nice';
    food='stunning';
    currency='funny';
}else{

    weather='nice';
    food='stunning';
    currency='funny';
}

var message = 'this is '+country+',the weather here is '+weather
    +',the food is '+food+',and currency is '+currency;

console.log(message);