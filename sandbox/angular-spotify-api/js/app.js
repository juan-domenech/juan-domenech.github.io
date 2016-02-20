var SpotifyAPIApp = angular.module('SpotifyAPIApp', [
  'ngRoute',
  'SpotifyAPIControllers',
  'SpotifyAPIFilters'
]);

SpotifyAPIApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/artists', {
        templateUrl: 'partials/artist-list.html',
        controller: 'ArtistListCtrl'
      }).
      when('/artists/:ArtistId', {
        templateUrl: 'partials/artistdetail.html',
        controller: 'ArtistDetailCtrl'
      }).
      otherwise({
        redirectTo: '/artists'
      });
  }]);

