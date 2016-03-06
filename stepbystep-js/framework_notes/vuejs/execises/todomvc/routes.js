/**
 * Created by patrick on 16/2/4.
 */

(function (app, Router) {

    'use strict';

    var router = new Router();

    ['all', 'active', 'completed'].forEach(function (visibility) {
        router.on(visibility, function () {
            app.visibility = visibility;
        });
    });

    router.configure({
        notfound: function () {
            window.location.hash = '';
            app.visibility = 'all';
        }
    });

    router.init();

})(app, Router);