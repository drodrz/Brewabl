'use strict';

angular.module('brewablApp')
  .controller('RegisterCtrl', function ($scope, djangoAuth, Validate, ngDialog) {
  	$scope.model = {'name':'','email':'','password':''};
  	$scope.complete = false;
    $scope.register = function(formData){
      $scope.errors = [];
      Validate.form_validation(formData,$scope.errors);
      if(!formData.$invalid){
        djangoAuth.register($scope.model.name,$scope.model.email,$scope.model.password1,$scope.model.password2)
        .then(function(data){
        	// success case
        	$scope.complete = true;
        },function(data){
        	// error case
        	$scope.errors = data;
        });
      }
    }
  });
