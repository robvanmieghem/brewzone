angular.module('brewzone', ['$strap.directives']).
  config(['$routeProvider', function($routeProvider) {
  $routeProvider.
  	  when('/', {templateUrl: 'partials/home.html'}).
      when('/state', {templateUrl: 'partials/state.html'}).
      when('/history', {templateUrl: 'partials/history.html', controller: BrewzoneController}).
      when('/settings', {templateUrl: 'partials/settings.html'}).
      otherwise({redirectTo: '/'});
}]).directive('chart', function () {
    return {
        restrict: 'A',
        link: function (scope, elem, attrs) {
        		var updateChart = function(data){
        			elem.empty();
    				$.jqplot(attrs.id,[ data ],{
    						axes:{
    			        	yaxis:{
    			        			tickOptions:{
    			        				formatString:'%.2f &nbsp;&#x2103'
    			        			}
    			        		}
    						},
    					    cursor: {
    					    		show: true,
    					    		zoom:true
    					        }
    						}
    						);
        		}
        
        		scope.$watch(attrs.ngModel, function(newValue, oldValue) {
        		    updateChart(newValue);
        		});
        	}
    	}
	}
		)
;
