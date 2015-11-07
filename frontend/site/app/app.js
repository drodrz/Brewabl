var brewablApp = angular.module('brewablApp', [
    'ngCookies',
    'ngResource',
    'ngSanitize',
    'ngRoute',
    'ngDialog',
])
    .config(function($httpProvider, $interpolateProvider, $routeProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $routeProvider.
            when("/", {
                templateUrl: "/app/components/home/homeView.html",
                controller: "homeController",
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }],
                }
            })
            .when('/passwordReset', {
                templateUrl: 'app/components/auth/views/passwordreset.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }],
                }
            })
            .when('/passwordResetConfirm/:firstToken/:passwordResetToken', {
                templateUrl: 'app/components/auth/views/passwordresetconfirm.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }],
                }
            })
            .when('/verifyEmail/:emailVerificationToken', {
                templateUrl: 'app/components/auth/views/verifyemail.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }],
                }
            })
            .when('/userProfile', {
                templateUrl: 'app/components/auth/views/userprofile.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }],
                }
            })
            .when('/passwordChange', {
                templateUrl: 'app/components/auth/views/passwordchange.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }],
                }
            })
            .when('/restricted', {
                templateUrl: 'app/components/auth/views/restricted.html',
                controller: 'RestrictedCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }],
                }
            })
            .when('/authRequired', {
                templateUrl: 'app/components/auth/views/authrequired.html',
                controller: 'AuthrequiredCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus(true);
                    }],
                }
            })
            .otherwise({redirectTo: '/'});
    })
    .run(function(djangoAuth){
        djangoAuth.initialize('/rest-auth', false);
    });
