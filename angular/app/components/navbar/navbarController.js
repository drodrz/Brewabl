'use strict';
//, $routeParams, djangoAuth, Validate
angular.module('brewablApp')
    .controller('navbarController', function ($scope, djangoAuth) {
        $scope.navbarActive = true;
    }
);