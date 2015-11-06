'use strict';

angular.module('brewablApp')
    .controller('homeController', function ($scope, djangoAuth) {
        $scope.homeActive = true;
    }
);
