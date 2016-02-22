
var SpotifyAPIControllers = angular.module('SpotifyAPIControllers', []);

// Artists Search (Main page)
SpotifyAPIControllers.controller('ArtistListCtrl', ['$scope', '$routeParams', '$http', '$location',

  // Function executed when we get an artist name at the URL Parameters
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

    $scope.typeEnter = function(Search) {

      // Make sure the user has entered something in Input (it might be a backspace)
      if (Search != undefined && Search != ''){

        // Search Artist with whatever we have in the search box
        $http.get('https://api.spotify.com/v1/search?q='+ Search +'&type=artist').success(function(data) {
          $scope.artists = data.artists.items;
          // After Enter Key detected send user to Albums choosing the first artist of the list
          $location.path("albums/"+data.artists.items[0].id+"/"+data.artists.items[0].name)
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

    // Get Album Thumbnail
    $http.get('https://api.spotify.com/v1/albums/'+ $routeParams.AlbumId).success(function(data) {
      $scope.AlbumThumbnail = data.images[1].url;

    });


    // Get Track List
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

    // Get Album Thumbnail
    $http.get('https://api.spotify.com/v1/tracks/'+ $routeParams.TrackId).success(function(data) {
      $scope.AlbumThumbnail = data.album.images[1].url;

    });

    $http.get('https://api.spotify.com/v1/tracks/'+ $routeParams.TrackId).success(function(data) {
      $scope.track = data;

      });

    $scope.TrackName = $routeParams.TrackName;
    $scope.AlbumName = $routeParams.AlbumName;
    $scope.ArtistName = $routeParams.ArtistName;

  }]
);
