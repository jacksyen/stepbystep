/**
 * Created by patrick on 16/3/5.
 */

var express = require('express');
var bodyParser = require('body-parser');

var app = express();
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

var apiKeys = ['foo', 'bar', 'bza'];
var repos = [
    {name: 'simonpatrick', url: 'http://github.com/simonpatrick'},
    {name: 'testless', url: 'http://github.com/testless'}
];
var users = [
    {name: 'simonpatrick'},
    {name: 'testless'}
];

function error(status, msg) {
    var err = new Error(msg);
    err.status = status;
    return err;
};

//pre-controller
app.use('/api', function (req, res, next) {
    var key = req.query['api-key'];
    if (!key) return next(error(400, 'api key required'));
    if (apiKeys.indexOf(key) < 0) return next('401', 'invalid api key');
    req.key = key;
    next(); //next doing another lookup
});

app.get('/api/users', function (req, res, next) {
    res.send(users);
});

app.get('/api/repos', function (req, res, next) {
    res.send(repos);
});

app.get('/api/user/:name/repo', function (req, res, next) {
    var name = req.params.name;
    var user = repos[name];
    if (user) res.send(user);
    else next();
});

app.use(function (req, res) {
    res.status(404);
    res.send({error: "Lame, can't find that"});
});

app.use(function (err, req, res, next) {
    // whatever you want here, feel free to populate
    // properties on `err` to treat it differently in here.
    res.status(err.status || 500);
    res.send({error: err.message});
});

app.listen(2595);
console.log('Express started on port 2595');



