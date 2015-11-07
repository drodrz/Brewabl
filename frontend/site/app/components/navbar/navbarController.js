'use strict';

angular.module('brewablApp')
    .controller('navbarController', function ($scope, $location, djangoAuth, ngDialog) {
        $scope.authenticated = false;
        // Wait for the status of authentication, set scope var to true if it resolves
        djangoAuth.authenticationStatus(true).then(function () {
            $scope.authenticated = true;
        });
        // Wait and respond to the logout event.
        $scope.$on('djangoAuth.logged_out', function() {
            $scope.authenticated = false;
        });
        // Wait and respond to the log in event.
        $scope.$on('djangoAuth.logged_in', function() {
            $scope.authenticated = true;
        });
        // If the user attempts to access a restricted page, redirect them back to the main page.
        $scope.$on('$routeChangeError', function(ev, current, previous, rejection){
            console.error("Unable to change routes.  Error: ", rejection)
            $location.path('/restricted').replace();
        });
        $scope.clickSignin = function () {
            ngDialog.open({
                template: 'app/components/auth/views/loginDialog.html',
                controller: '',
                className: 'brewabl-dialog-theme',
            }).closePromise.then(function(dialogResult){
                console.log(dialogResult.value)
            })
        };
        $scope.clickRegister = function () {
            ngDialog.open({
                template: 'app/components/auth/views/registerDialog.html',
                className: 'brewabl-dialog-theme',
            }).closePromise.then(function(dialogResult){
                console.log(dialogResult.value)
            })
        };
        $scope.clickLogout = function () {
            ngDialog.open({
                template: 'app/components/auth/views/logoutDialog.html',
                className: 'brewabl-dialog-theme',
            }).closePromise.then(function(dialogResult){
                console.log(dialogResult.value)
            })
        };
    });