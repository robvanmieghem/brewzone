angular.module('brewzone', [])
.directive('chart', function () {
    return {
        restrict: 'A',
        link: function (scope, elem, attrs) {
        		var updateChart = function(data){
        			elem.empty();
    				$.jqplot(attrs.id,[ data ],{
    					
    					series:[{showMarker:false}],
    					// You can specify options for all axes on the plot at once with
    				      // the axesDefaults object.  Here, we're using a canvas renderer
    				      // to draw the axis label which allows rotated text.
    				      axesDefaults: {
    				        labelRenderer: $.jqplot.CanvasAxisLabelRenderer,
    				        min: 0,
    				        labelOptions: {
    				            fontFamily: 'Georgia, Serif',
    				            fontSize: '10pt'
    				          }
    				      },
    				      // An axes object holds options for all axes.
    				      // Allowable axes are xaxis, x2axis, yaxis, y2axis, y3axis, ...
    				      // Up to 9 y axes are supported.
    				      axes: {
    				        // options for each axis are specified in seperate option objects.
    				        xaxis: {
    				          label: "Sugar to add (g/L)",
    				          // Turn off "padding".  This will allow data point to lie on the
    				          // edges of the grid.  Default padding is 1.2 and will keep all
    				          // points inside the bounds of the grid.
    				          pad: 0
    				        },
    				        yaxis: {
    				          label: "CO2 level (g/L)",
    				          pad: 0
    				        }
    				      },
    					
    					    cursor: {
    					    		show: true,
    					    		showTooltip: false,
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
