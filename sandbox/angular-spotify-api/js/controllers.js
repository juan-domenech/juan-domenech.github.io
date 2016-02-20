var SpotifyAPIControllers = angular.module('SpotifyAPIControllers', []);

SpotifyAPIControllers.controller('ArtistListCtrl', ['$scope', '$http',
  function ($scope, $http) {
    $http.get('artists.json').success(function(data) {
      $scope.artists = data.artists.items;
      console.log(data)
    });

    $scope.orderProp = 'age';
  }]);

SpotifyAPIControllers.controller('ArtistDetailCtrl', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {
    $http.get('artists/' + $routeParams.phoneId + '.json').success(function(data) {
      $scope.artist = data;
      $scope.mainImageUrl = data.images[0];
    });

    $scope.setImage = function(imageUrl) {
      $scope.mainImageUrl = imageUrl;
    };
  }]);