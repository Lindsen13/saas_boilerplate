$(document).ready(function () {
   $('#username').keyup(function (e) {
      var username = $('#username').val();

      if (username != '') {

         $.ajax({
            url: '/check_username_exists',
            type: 'post',
            data: { username: username },
            success: function (response) {
               if (response == "true") {
                  $('#uname_response').html("Username taken").css({ 'color': 'red', 'text-align': 'right' });
               } else {
                  $('#uname_response').html("Available").css({ 'color': 'blue', 'text-align': 'right' });
                  $('#button').removeAttr('disabled');
               }
            }
         });
      } else {
         $("#uname_response").html("");
      }
   })
})