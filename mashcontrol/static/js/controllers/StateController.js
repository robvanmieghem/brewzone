function StateController($scope){
	
	$scope.startRecording = function(){
		$scope.state.recording = true;
	};
	
	$scope.stopRecording = function(){
		$scope.state.recording = false;
	};
};