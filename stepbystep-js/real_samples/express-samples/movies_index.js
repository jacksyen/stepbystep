/**
 * Created by patrick on 16/3/5.
 */
var express = require('express'),
    fs = require('fs'),
    port = process.env.PORT || 2595,
    bodyParser = require('body-parser');

var bookings = [];
var app = express();
var ejs = require('ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.set("view option", {
    layout: false,
    debug: true
});

//app.set('view engine', ejs);
app.engine('html',ejs.renderFile)
app.set('views', __dirname + '/public/views');
app.use(express.static(__dirname + '/public'));

app.get('/', function (req, res) {
    res.render('movies_index.html');
});

app.get('/movies', function (req, res) {
    var movies = require('./data/movies.json');
    res.json(movies);
});

app.get('/bookings', function (req, res) {
    res.json(bookings);
});

app.post('/book', function (req, res) {
    var data = {
        'qty': req.body.qty,
        'date': req.body.date,
        'id': req.body.movie_id,
        'name': req.body.movie_name
    };
    bookings.push(data);
    res.json(bookings);
});

app.listen(2595, function () {
    console.log("staring in " + 2595);
});


