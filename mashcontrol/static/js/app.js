angular.module('brewzone', ['$strap.directives', 'brewzoneServices']).
  config(['$routeProvider', function($routeProvider) {
  $routeProvider.
  	  when('/', {templateUrl: 'partials/home.html'}).
      when('/state', {templateUrl: 'partials/state.html', controller: StateController}).
      when('/schemes', {templateUrl: 'partials/schemes.html'}).
      when('/history', {templateUrl: 'partials/history.html', controller: HistoryController}).
      when('/settings', {templateUrl: 'partials/settings.html', controller: SettingsController}).
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
