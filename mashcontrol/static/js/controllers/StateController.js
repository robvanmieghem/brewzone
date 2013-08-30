function StateController($scope, $http, $filter){
	
	$scope.startRecording = function(){
		var start = $filter('date')(new Date(), 'yyyy-MM-ddTHH:mm:ssZ');
		$http.put('../hardware/recorder',{recording:true, start:start});
	};
	
	$scope.stopRecording = function(){
		$http.put('../hardware/recorder',{recording:false});
	};
};