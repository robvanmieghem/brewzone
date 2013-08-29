function HistoryController($scope, Recording) {
	$scope.recordings = Recording.query();
	$scope.current = {
			selectedRecording:{}
	};
};