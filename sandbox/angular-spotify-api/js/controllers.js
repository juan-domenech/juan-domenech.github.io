
var SpotifyAPIControllers = angular.module('SpotifyAPIControllers', []);

// Artists Search (Main page)
SpotifyAPIControllers.controller('ArtistListCtrl', ['$scope', '$routeParams', '$http', '$location',

  // Function executed when we get an artist name on URL Parameters
  function ($scope, $routeParams, $http, $location) {

    // Make sure we have something in the URL to work with
    if ($routeParams.Search){
      // Search Artist using the string in the URL
      $http.get('https://api.spotify.com/v1/search?q='+ $routeParams.Search +'&type=artist').success(function(data) {
        $scope.artists = data.artists.items;
      });
    }

    //
    // Function executed everytime Input has changed
    $scope.typeSearch = function(Search) {

      // Make sure the user has entered something in Input (it might be a backspace)
      if (Search != undefined && Search != ''){

        // Search Artist with whatever we have in the search box
        $http.get('https://api.spotify.com/v1/search?q='+ Search +'&type=artist').success(function(data) {
          $scope.artists = data.artists.items;
        });
      }
    };
  }]
);


// Show Albums
SpotifyAPIControllers.controller('AlbumsCtrl', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {

    $http.get('https://api.spotify.com/v1/artists/'+ $routeParams.ArtistId +'/albums').success(function(data) {
      $scope.albums = data.items;
      });

    $scope.ArtistId = $routeParams.ArtistId;
    $scope.ArtistName = $routeParams.ArtistName;

  }]
);


// Show Tracks
SpotifyAPIControllers.controller('TracksCtrl', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {

    $http.get('https://api.spotify.com/v1/albums/'+ $routeParams.AlbumId +'/tracks').success(function(data) {
      $scope.tracks = data.items;
      });

    $scope.AlbumName = $routeParams.AlbumName;
    $scope.ArtistName = $routeParams.ArtistName;

  }]
);


// Play Track
SpotifyAPIControllers.controller('PlayCtrl', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {

    $http.get('https://api.spotify.com/v1/tracks/'+ $routeParams.TrackId).success(function(data) {
      $scope.track = data;
      console.log(data)
      });

    $scope.TrackName = $routeParams.TrackName;
    $scope.AlbumName = $routeParams.AlbumName;
    $scope.ArtistName = $routeParams.ArtistName;

  }]
);
