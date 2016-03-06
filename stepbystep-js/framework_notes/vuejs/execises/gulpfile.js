var gulp = require('gulp');
var qunit = require('gulp-qunit');
var jshint = require('gulp-jshint');
var htmlhint = require('gulp-htmlhint');
var csslint = require('gulp-csslint');

gulp.task('default', function () {

});

gulp.task('test', function () {
    return gulp.src('travis-stats/test.html')
        .pipe(qunit({'phantomjs-options': ['--ignore-ssh-errors=true']}));
});

gulp.task('jslint', function () {
    return gulp.src('travis-stats/*.js')
        .pipe(jshint()).pipe(jshint().reporter('default')).pipe(jshint.reporter('fail'));
});

gulp.task('htmllint', function () {
    return gulp.src(['travis-stats/*.html'])
        .pipe(htmlhint()).pipe(htmlhint.reporter()).pipe(htmlhint.failReporter())
});

gulp.task('csslint', function () {
    return gulp.src('travis-stat/*.css')
        .pipe(csslint()).pipe(csslint.reporter()).pipe(csslint.failReporter());
});
