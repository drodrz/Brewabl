'use strict';

angular.module('brewablApp')
    .controller('navbarController', function ($scope, djangoAuth) {
        $scope.navbarActive = true;
    }
);