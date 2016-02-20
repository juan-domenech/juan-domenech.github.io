var SpotifyAPIControllers = angular.module('SpotifyAPIControllers', []);

SpotifyAPIControllers.controller('ArtistListCtrl', ['$scope', '$routeParams', '$http',
  function ($scope, $routeParams, $http) {
    $http.get('https://api.spotify.com/v1/search?q='+ $routeParams.Search +'&type=artist').success(function(data) {
      $scope.artists = data.artists.items;
      //console.log("scope.artists",$scope.artists)
      //console.log("routeParams",$routeParams.Search)
    });

    $scope.orderProp = 'age';
  }]);

SpotifyAPIControllers.controller('ArtistDetailCtrl', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {

    $http.get('https://api.spotify.com/v1/artists/'+ $routeParams.ArtistId).success(function(data) {
      $scope.ArtistName = data.name;

      //console.log($scope.ArtistName)

      });

    $http.get('https://api.spotify.com/v1/artists/'+ $routeParams.ArtistId +'/albums').success(function(data) {
      $scope.albums = data.items;
      //$scope.mainImageUrl = data.images[0];
      //console.log($routeParams.ArtistId)
      //console.log($scope.albums)

      });

    //$scope.setImage = function(imageUrl) {
    //  $scope.mainImageUrl = imageUrl;
    //};
  }]);