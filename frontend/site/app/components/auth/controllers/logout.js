'use strict';

angular.module('brewablApp')
  .controller('LogoutCtrl', function ($scope, $location, djangoAuth) {
    djangoAuth.logout();
  });
