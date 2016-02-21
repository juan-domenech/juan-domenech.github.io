//angular.module('SpotifyAPIFilters', []).filter('checkmark', function() {
//  return function(input) {
//    return input ? '\u2713' : '\u2718';
//  };
//});

angular.module('SpotifyAPIFilters', []).config(function($sceDelegateProvider) {
  $sceDelegateProvider.resourceUrlWhitelist([
    // Allow same origin resource loads.
    'self',
    // Allow loading from our assets domain.  Notice the difference between * and **.
    'https://*.scdn.co/**'
  ]);
});
