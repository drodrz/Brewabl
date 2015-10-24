'use strict';
//, $routeParams, djangoAuth, Validate
angular.module('brewablApp')
    .controller('homeController', function ($scope, djangoAuth) {
        $scope.homeActive = true;
    }
);
