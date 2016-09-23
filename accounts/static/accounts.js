var initialize = function(navigator, user, token, urls) {
    console.log(navigator)
    $('#id_login').on('click', function() {
        navigator.id.request();
    });
    $('#id_logout').on('click', function(){
        navigator.id.logout();
    });

    navigator.id.watch({ loggedInUser: user, 
        onlogin: function(assertion) {
            var deferred = $.post(urls.login,
                   { assertion: assertion, csrfmiddlewaretoken: token }
            );
            deferred.done(function() { window.location.reload(); });
            deferred.fail(function() { navigator.id.logout(); });
        },
        onlogout: function() {i
            var deferred = $.post(urls.logout, {csrfmiddlewaretoken: token} )
            deferred.done(function() { window.location.reload(); });
            deferred.fail(function() { navigator.id.logout(); });
        }
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};
