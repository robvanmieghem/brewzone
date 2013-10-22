primingController = function($scope){
	var temperature_adjustment = [
			3.4,
			3.3,
			3.2,
			3.1,
			3.0,
			2.9,
			2.8,
			2.7,
			2.6,
			2.5,
			2.4,
			2.3,
			2.2,
			2.15,
			2.1,
			2.05,
			2.0,
			1.95,
			1.9,
			1.85,
			1.8,
			1.75,
			1.7
		]
	
	$scope.selectedTemperature = 15;
	$scope.co2forSugarTable	=[];
	
	$scope.co2ForSugar = function(sugar){
		var temperatureCorrection = temperature_adjustment[$scope.selectedTemperature];
		return (sugar * 0.46) + temperatureCorrection;
	}
	
	$scope.sugarForCo2 = function(co2){
		var temperatureCorrection = temperature_adjustment[$scope.selectedTemperature];
		return (co2 - temperatureCorrection) * (1/0.46);
	}
	
	$scope.updateCO2ForSugar = function(){
		
		var co2forSugarTable = []
		for (var i=0;i<12;i++)
		{ 
			co2forSugarTable.push([i,$scope.co2ForSugar(i)]);
		}
		$scope.co2forSugarTable = co2forSugarTable;
	};
	
	$scope.updateCO2ForSugar();
	
	$scope.$watch('selectedTemperature', function(newValue, oldValue) {
		$scope.updateCO2ForSugar();
	});
	
	$scope.bottlingvessel = 'bucket';
	$scope.bucketsize = 20;
	$scope.bottlesize = 0.33;
	$scope.saturationGramLiter = 5.5;
	
	
	$scope.updatedSaturation = function(){
		$scope.sugarGramLiter = $scope.sugarForCo2($scope.saturationGramLiter);
		$scope.sugarPerBottle = $scope.sugarGramLiter * $scope.bottlesize;
		$scope.sugarGramTotal = $scope.sugarGramLiter * $scope.bucketsize;
	};
	
	$scope.updatedSaturation();
	
	$scope.updatedBucketSize = function(){
		$scope.sugarGramTotal = $scope.sugarGramLiter * $scope.bucketsize;
	};
	
	$scope.updatedBottleSize = function(){
		$scope.sugarPerBottle = $scope.sugarGramLiter * $scope.bottlesize;
	};
	
	$scope.updatedSugarPerBottle = function(){
		$scope.sugarGramLiter = $scope.sugarPerBottle / $scope.bottlesize;
		$scope.sugarGramTotal = $scope.sugarGramLiter * $scope.bucketsize;
		$scope.saturationGramLiter = $scope.co2ForSugar($scope.sugarGramLiter);
	};
	
	$scope.updatedSugarGramTotal = function(){
		$scope.sugarGramLiter = $scope.sugarGramTotal / $scope.bucketsize;
		$scope.sugarPerBottle = $scope.sugarGramLiter * $scope.bottlesize;
		$scope.saturationGramLiter = $scope.co2ForSugar($scope.sugarGramLiter);
	};

	$scope.updatedSugarGramLiter = function(){
		$scope.sugarPerBottle = $scope.sugarGramLiter * $scope.bottlesize;
		$scope.sugarGramTotal = $scope.sugarGramLiter * $scope.bucketsize;
		$scope.saturationGramLiter = $scope.co2ForSugar($scope.sugarGramLiter);
	};
	
}