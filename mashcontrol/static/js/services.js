angular.module('brewzoneServices', ['ngResource']).
    factory('Recording', function($resource){
  return $resource('../recordings/:startTime', {}, {
  });
});