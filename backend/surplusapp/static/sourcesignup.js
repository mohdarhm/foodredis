$(document).ready(function() {
    var submitButton = $('#signup-button');
    var timeout;
    var usernameExistsDiv = $('#username-exists');
    var usernameDoesntExistDiv = $('#username-doesnt-exist');

    $('#username').on('input', function() {
        clearTimeout(timeout);

        timeout = setTimeout(function() {
            var username = $(this).val();
            $.ajax({
                url: '/check_username/',
                data: {
                    'username': username
                },
                dataType: 'json',
                success: function(data) {
                    if (data.exists) {
                        usernameExistsDiv.html('Username already exists.').addClass('error');
                        usernameDoesntExistDiv.html('').removeClass('error');
                        submitButton.prop('disabled', true);
                    } else {
                        usernameExistsDiv.html('');
                        usernameDoesntExistDiv.html('').removeClass('error');
                        submitButton.prop('disabled', false);
                    }
                },
                error: function(xhr, status, error) {
                    // Handle errors, e.g., display an error message in another container
                    $('#error-message').html('Error: ' + error);
                }
            });
        }.bind(this), 500);
    });
});
