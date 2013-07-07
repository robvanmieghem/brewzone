function BrewzoneController($scope, $http, $timeout) {
	
	$scope.updateHardwareState = function(repeatIn){
		$http.get('../hardware').
	  		success(function(data, status, headers, config) {
		    	$scope.hardware = data;
		  	}).
		  	error(function(data, status, headers, config) {
			  $scope.hardware = {}
		  	});
		$timeout($scope.updateHardwareState, repeatIn)
	};
	
	$scope.updateHardwareState(1000);
	
	$scope.mashschemedata = [];
	
	$scope.mashscheme = {
			start : {temperature : 57},
			beta : {temperature:63, length:30},
			alpha : {temperature:73, length:30},
			mashout : {temperature:79}
			
	}


	$scope.updateMashSchemeDataFromScheme = function(){

		var newValue = $scope.mashscheme;
		var mashdata = [];
		var temperature = parseFloat(newValue.start.temperature);
		var time = 0;
		mashdata.push([time,temperature]);
		
		time += parseFloat(newValue.beta.temperature) - temperature;
		temperature = parseFloat(newValue.beta.temperature);
		mashdata.push([time,temperature]);
		time += parseFloat(newValue.beta.length);
		mashdata.push([time,temperature]);
		
		
		time += parseFloat(newValue.alpha.temperature) - temperature;
		temperature = parseFloat(newValue.alpha.temperature);
		mashdata.push([time,temperature]);
		time += parseFloat(newValue.alpha.length);
		mashdata.push([time,temperature]);
		

		time += parseFloat(newValue.mashout.temperature) - temperature;
		temperature = parseFloat(newValue.mashout.temperature);
		mashdata.push([time,temperature]);
		
		$scope.mashschemedata = mashdata;
		
	}
	
	$scope.$watch('mashscheme', function(newValue, oldValue){
		if (!newValue){
			return;
		}
		$scope.updateMashSchemeDataFromScheme();
	});
}
