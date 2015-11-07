'use strict';

angular.module('brewablApp')
  .controller('LoginCtrl', function ($scope, $location, djangoAuth, Validate, ngDialog) {
    $scope.model = {'email':'','password':''};
  	$scope.complete = false;
    $scope.login = function(formData){
      $scope.errors = [];
      Validate.form_validation(formData,$scope.errors);
      if(!formData.$invalid){
        djangoAuth.login($scope.model.email, $scope.model.password)
        .then(function(data){
        	// success case
            ngDialog.close()
        	$location.path("/");
        },function(data){
        	// error case
        	$scope.errors = data;
        });
      }
    }
  });
