var SpotifyAPIApp = angular.module('SpotifyAPIApp', [
  'ngRoute',
  'SpotifyAPIControllers',
  'SpotifyAPIFilters'
]);

SpotifyAPIApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/artists/', {
        templateUrl: 'partials/search.html',
        controller: 'ArtistListCtrl'
      }).
      when('/artists/:Search', {
        templateUrl: 'partials/search.html',
        controller: 'ArtistListCtrl'
      }).
      when('/albums/:ArtistId', {
        templateUrl: 'partials/albums.html',
        controller: 'AlbumsCtrl'
      }).
      when('/albums/:ArtistId/:ArtistName', {
        templateUrl: 'partials/albums.html',
        controller: 'AlbumsCtrl'
      }).
      when('/tracks/:AlbumId/:AlbumName/:ArtistName', {
        templateUrl: 'partials/tracks.html',
        controller: 'TracksCtrl'
      }).
      otherwise({
        redirectTo: '/artists'
      });
  }]);

