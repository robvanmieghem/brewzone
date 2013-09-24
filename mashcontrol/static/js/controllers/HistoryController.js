function HistoryController($scope, Recording) {
	$scope.recordings = Recording.query();
	$scope.current = {
			selectedRecording:{}
	};
	
	$scope.deleteRecording = function(recording){
		Recording.delete({startTime:recording.start})
		$scope.current.selectedRecording = {};
		$scope.recordings = Recording.query();
	};
	
	$scope.selectRecording= function(recording){
		$scope.current.selectedRecording = recording;
		$scope.current.selectedRecording = Recording.get({startTime:recording.start})
	};
};