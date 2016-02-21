
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
        //console.log("scope.artists",$scope.artists)
        //console.log("routeParams",$routeParams.Search)
      });
    }
    //console.log($location.path());
    //$scope.location = $location;
    //$scope.orderProp = 'age';

    //
    // Function executed everytime Input has changed
    $scope.typeSearch = function(Search) {
      //$scope.mainImageUrl = imageUrl;
      //console.log(Search);

      // Make sure the user has entered something in Input (it might be a backspace)
      if (Search != undefined && Search != ''){

        // Search Artist with whatever we have in the search box
        $http.get('https://api.spotify.com/v1/search?q='+ Search +'&type=artist').success(function(data) {
          $scope.artists = data.artists.items;
          //console.log("scope.artists",$scope.artists)
          //console.log("routeParams",$routeParams.Search)
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
      //$scope.mainImageUrl = data.images[0];
      //console.log($routeParams.ArtistId)
      //console.log($scope.albums)

      });

    $scope.ArtistName = $routeParams.ArtistName;

    //$scope.setImage = function(imageUrl) {
    //  $scope.mainImageUrl = imageUrl;
    //};
  }]
);


// Show Tracks
SpotifyAPIControllers.controller('TracksCtrl', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {

    $http.get('https://api.spotify.com/v1/albums/'+ $routeParams.AlbumId +'/tracks').success(function(data) {
      $scope.tracks = data.items;
      //console.log($scope.tracks)
      });

    $scope.AlbumName = $routeParams.AlbumName;
    $scope.ArtistName = $routeParams.ArtistName;

  }]
);