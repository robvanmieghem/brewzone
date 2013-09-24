function SettingsController($scope, $http){
	$scope.raspberrypi = {}
	
	$scope.UpdateRPiInfo = function(){
		$http.get('../hardware/pi').
  		success(function(data, status, headers, config) {
  			$scope.raspberrypi.hwinfo  = data;
	  	});
		 
	};
};