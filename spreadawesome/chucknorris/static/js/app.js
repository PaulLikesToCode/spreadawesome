var app = angular.module('chucknorris', ['ngResource', 'ngRoute', 'ui.bootstrap']);

// app.config(['$httpProvider', function($httpProvider) {
// 	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
// 	$httpProvider.defaultsxsrfHeaderName = 'X-CSRFToken';
// }]);

// app.factory('api', function($resource) {
// 	function add_auth_header(data, headersGetter) {
// 		var headers = headersGetter();
// 		headers['Authorization'] = ('Basic ' + btoa(data.username + ':' + data.password));
// 	}
// 	return {
// 		auth: $resource('/api/auth\\/', {}, {
// 			login: {method: 'POST', transformRequest: add_auth_header},
// 			logout: {method: 'DELETE'}
// 		}),
// 		users: $resource('/api/users\\/', {}, {create: {method:'POST'}})
// 	};
// });

app.factory('quotes', [function() {
	var q = {
		quotes: []
	};
	return q;
}]);

app.controller('ModalDemoCtrl', function($scope, $modal) {
	$scope.open = function() {
	    var modalInstance = $modal.open({
	      templateUrl: 'myModalContent.html',
	    });
	};
});

app.controller('facebook', ['$scope', function($scope) {
	$scope.getFriends = function() {
		FB.api(
    		"/me/friends",
    		function (response) {
      		if (response && !response.error) {
        		console.log(response);
      			}
   			}
		);
	}
}]);

app.controller('getRandomFact', ['$scope', '$http', 'quotes', function($scope, $http, quotes) {

	$scope.getChuckQuote = function() {
		$http.get('http://api.icndb.com/jokes/random').
			success(function(data, status) {
				$scope.quote = (data.value.joke).replace(/&quot;/g, '"');
			}).error(function(data,status) {
				$scope.quote = "Sorry, Chuck Norris is busy right now";
			});
	}

	$scope.getCustomQuote = function() {
		$http.get('http://api.icndb.com/jokes/random?firstName='+$scope.person.first_name+'&lastName='+$scope.person.last_name).
			success(function(data, status) {
				$scope.quote = (data.value.joke).replace(/&quot;/g, '"');
			}).error(function(data,status) {
				$scope.quote = 'Sorry, Chuck Norris is busy right now.';
			});
		}

	$scope.saveQuote = function() {
		quotes.quotes.push($scope.quote);
	}
}]);

app.controller('showQuotes', ['$scope', '$http', 'quotes', function($scope, $http, quotes) {
	$scope.quotes = quotes.quotes;
	$scope.dynamicTooltip = 'remove';
	$scope.removeQuote = function(index) {
		$scope.quotes.splice(index, 1);	
	}

	$scope.tweetQuote = function(index) {
		if (typeof localStorage['oauth_token'] === 'undefined') {
			alert("Please log in to send a tweet");
		} else {
			var tweetContent = $scope.quotes[index];
			var data = {
				twitter_handle: localStorage['twitter_handle'],
				message: tweetContent,
				oauth_token: localStorage['oauth_token'],
				oauth_token_secret: localStorage['oauth_token_secret'],
			}
			$http.post('/send_tweet/', data).
				success(function(data) {
					// Do something else here, a timeout alert or something
					console.log(data.message);
				}).
				error(function() {
					// Do something else here, handle the error
					console.log('sorry');
				});
		}
	}
}]);





