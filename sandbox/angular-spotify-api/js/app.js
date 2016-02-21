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
      when('/albums/:ArtistId/:ArtistName', {
        templateUrl: 'partials/albums.html',
        controller: 'AlbumsCtrl'
      }).
      when('/tracks/:AlbumId/:AlbumName/:ArtistName', {
        templateUrl: 'partials/tracks.html',
        controller: 'TracksCtrl'
      }).
      when('/play/:TrackId/:TrackName/:AlbumName/:ArtistName', {
        templateUrl: 'partials/play.html',
        controller: 'PlayCtrl'
      }).
      otherwise({
        redirectTo: '/artists'
      });
  }]);
