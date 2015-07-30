function compare(a,b) {
    if (a._id < b._id)
        return -1;
    if (a._id > b._id)
        return 1;
    return 0;
}

var myApp = angular.module('saltdashboard', []).config(function($sceProvider) { $sceProvider.enabled(false); });

myApp.controller('SaltController', ['$scope', '$log', '$http', function($scope, $log, $http) {
    $scope.salt_return = {};
    function get_jobs(){
        $http.get('/api/jobs').
            success(function(data, status, headers, config) {
                $scope.jobs = data['jobs'].sort();
                return $scope.jobs;
            }).error(function(error) {
                $log.log(error);
            });
    };
    function get_job(jid){
        $http.get('/api/jobs/' + jid).
            success(function(data, status, headers, config) {
                $scope.job_data = data;
            }).error(function(error) {
                $log.log(error);
            });
    };
    $scope.get_salt_return = function(jid){
        if ($scope.salt_return[jid] === undefined) {
            $http.get('/api/returns/' + jid).
                success(function(data, status, headers, config) {
                    $scope.salt_return[jid] = data;
                }).error(function(error) {
                    $log.log(error);
                });
        };
    };
    get_jobs();
}]);
