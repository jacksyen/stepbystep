/**
 * Created by patrick on 15/12/16.
 */

var apiURL = 'https://api.github.com/repos/vuejs/vue/commits?per_page=3&sha='
var isPhantom = navigator.userAgent.indexOf('PhantomJS') > -1

/**
 * Test Mocks
 * @type {{master: *[], dev: *[]}}
 */
var mocks = {
    master: [{
        sha: '111111111111',
        commit: {message: 'one', author: {name: 'simonpatrick', date: '2014-10-15T13:52:58Z'}}
    }, {
        sha: '111111111111',
        commit: {message: 'hi', author: {name: 'simonpatrick', date: '2014-10-15T13:52:58Z'}}
    }, {sha: '111111111111', commit: {message: 'hi', author: {name: 'simonpatrick', date: '2014-10-15T13:52:58Z'}}}],
    dev: [{
        sha: '222222222222',
        commit: {message: 'two', author: {name: 'simonpatrick', date: '2014-10-15T13:52:58Z'}}
    }, {
        sha: '111111111111',
        commit: {message: 'hi', author: {name: 'simonpatrick', date: '2014-10-15T13:52:58Z'}}
    }, {sha: '111111111111', commit: {message: 'hi', author: {name: 'simonpatrick', date: '2014-10-15T13:52:58Z'}}}]
};

var demo = new Vue({
    el: '#demo',
    data: {
        branches: ['master', 'dev'],
        currentBranch: 'master',
        commits: null
    },
    created: function () {
        this.fetchData()
    },
    watch: {
        currentBranch: 'fetchData'
    },
    filters: {
        truncate: function (v) {
            var newline = v.indexOf('\n');
            return newline > 0 ? v.slice(0, newline) : v
        },
        formatDate: function (v) {
            return v.replace(/T|Z/g, '')
        }
    },
    methods: {
        fetchData: function () {
            //casperJS fails at cross-domain XHR even with --web-security=no
            if (isPhantom) {
                return mockData.call(this)
            }
            var xhr = new XMLHttpRequest();
            var self = this;
            xhr.open('GET', apiURL + self.currentBranch);
            xhr.onload = function () {
                self.commits = JSON.parse(xhr.responseText);
                console.log(self.commits[0].html_url)
            };
            xhr.send()
        }
    }
});

