function BrewzoneController($scope, $http) {

	$scope.plotdata = [1,2,3,6,7,18,17,2];
	
	$scope.changeplotdata = function(){
		$scope.plotdata = [1,2,5,9,23,5,19];
	}
	
}
