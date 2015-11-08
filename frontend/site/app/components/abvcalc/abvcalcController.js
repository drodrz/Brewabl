'use strict';

angular.module('brewablApp')
    .controller('abvcalcController', function ($scope, $location) {
        $scope.og = 1.052;
        $scope.fg = 1.008;
        $scope.abv = 5.78;

        $scope.calcAbv = function () {
            // Formula courtesy of http://homebrew.stackexchange.com/questions/2924/calculating-alcohol-by-volume
            console.log('Hello from calcAbv');
            $scope.abv = ((76.08*($scope.og-$scope.fg)/(1.775-$scope.og))*($scope.fg/0.794))
        };
    });