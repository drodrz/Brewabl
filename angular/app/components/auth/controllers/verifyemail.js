'use strict';

angular.module('brewablApp')
  .controller('VerifyemailCtrl', function ($scope, $routeParams, djangoAuth) {
    djangoAuth.verify($routeParams["emailVerificationToken"]).then(function(data){
    	$scope.success = true;
    },function(data){
    	$scope.failure = false;
    });
  });
