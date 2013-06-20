angular.module('brewzone', ['$strap.directives']).
  config(['$routeProvider', function($routeProvider) {
  $routeProvider.
  	  when('/', {templateUrl: 'partials/home.html'}).
      when('/state', {templateUrl: 'partials/state.html',   controller: BrewzoneController}).
      when('/history', {templateUrl: 'partials/history.html', controller: BrewzoneController}).
      when('/settings', {templateUrl: 'partials/settings.html', controller: BrewzoneController}).
      otherwise({redirectTo: '/'});
}]).directive('chart', function () {
    return {
        restrict: 'A',
        link: function (scope, elem, attrs) {
        		var updateChart = function(data){
        			elem.empty();
    				$.jqplot(elem.attr('id'),[ data ]);
        		}
        
        		scope.$watch(attrs.ngModel, function(newValue, oldValue) {
        		     if(newValue) {
        		    	updateChart(newValue);
        		     }
        		});
        	}
    	}
	}
		)
;
