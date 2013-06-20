function BrewzoneController($scope, $http) {

	$scope.plotdata = [1,2,3,6,7,18,17,2,16];
	
	$scope.changeplotdata = function(linear){
	    if (linear){
	        $scope.plotdata = [1,2,3,4,5,6,7,8,9];
	    }
	    else{
		    $scope.plotdata = [1,2,3,6,7,18,17,2,16];
		   }
	}
	

	$scope.mashdata = [];
	
	$scope.mashscheme = {
			start : {temperature : 57},
			beta : {temperature:63, length:30},
			alpha : {temperature:73, length:30},
			mashout : {temperature:80}
			
	}


	$scope.updateMashDataFromScheme = function(){

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
		
		$scope.mashdata = mashdata;
		
	}
	
	$scope.$watch('mashscheme', function(newValue, oldValue){
		if (!newValue){
			return;
		}
		$scope.updateMashDataFromScheme();
	});
}
