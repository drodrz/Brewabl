'use strict';

angular.module('brewablApp')
  .controller('LogoutCtrl', function ($scope, $location, djangoAuth, ngDialog) {
    djangoAuth.logout();
  });
