function StateController($scope, $http){
	
	$scope.startRecording = function(){
			$http.put('../hardware/recorder',{recording:true});
	};
	
	$scope.stopRecording = function(){
		$http.put('../hardware/recorder',{recording:false});
	};
};