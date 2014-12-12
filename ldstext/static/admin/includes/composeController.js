        // Load the multi-select module
var myApp = angular.module('myApp', [ 'multi-select' ]).config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

// Controller
myApp.controller( 'main' , [ '$scope' , function ($scope) {               

    $scope.resultData = [];
 
    // Modern web browsers with groups
    $scope.contactSelectionList = [
        {
            name: '<strong>Contact Groups</strong>',
            multiSelectGroup: true
        },
        {                        
            name: 'Bishopric',
			group: true,
            ticked: false
        },
        {                        
            name: 'Ward Council',
			group: true,
            ticked: false
        },
        {                        
            name: 'Elder\'s Quorum 1',
			group: true,
            ticked: false
        },
        {                        
            name: 'Elder\'s Quorum 2',
			group: true,
            ticked: false
        },
        {                        
            name: 'Relief Society',
			group: true,
            ticked: false
        },
        {                        
            name: 'FHE Group Leaders',
			group: true,
            ticked: false
        },
        {
            multiSelectGroup: false
        },
        {
            name: '<strong>Individuals</strong>',
            multiSelectGroup: true
        },
        {                        
            name: 'Bishop Roberts',
			group: false,
            ticked: false
        },
        {                        
            name: 'Jared Carter',
			group: false,
            ticked: false
        },
        {                        
            name: 'Natacia Snow',
			group: false,
            ticked: false
        },
        {                        
            name: 'Rick Mangum',
			group: false,
            ticked: false
        },
        {                        
            name: 'James Petmecky',
			group: false,
            ticked: false
        },
        {
            multiSelectGroup: false
        }
    ];
}]); 

