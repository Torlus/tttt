/*global angular*/
(function () {
    "use strict";

    var app = angular.module('frontend', ['ng-admin']);

    app.config(function (NgAdminConfigurationProvider) {
        var nga = NgAdminConfigurationProvider;

        // set the main API endpoint for this admin
        var app = nga.application('Tiny Time Tracking Tool')
            .baseApiUrl('http://localhost:8000/api/');

        // define an entity mapped by the http://localhost:3000/posts endpoint
        var category = nga.entity('categories');
        app.addEntity(category);

        // set the list of fields to map in each post view
        // post.dashboardView().fields(/* see example below */);
        // post.listView().fields(/* see example below */);
        // post.creationView().fields(/* see example below */);
        // post.editionView().fields(/* see example below */);

        nga.configure(app);
    });
}());
