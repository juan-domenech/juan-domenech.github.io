var SpotifyAPIApp = angular.module('SpotifyAPIApp', [
  'ngRoute',
  'SpotifyAPIControllers',
  'SpotifyAPIFilters'
]);

SpotifyAPIApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/artists/:Search', {
        templateUrl: 'partials/search.html',
        controller: 'ArtistListCtrl'
      }).
      when('/artist/:ArtistId', {
        templateUrl: 'partials/albums.html',
        controller: 'ArtistDetailCtrl'
      }).
      otherwise({
        redirectTo: '/artists'
      });
  }]);

