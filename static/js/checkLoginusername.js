$(document).ready(function(){
    $('#username').change( function(e){
        var username = $('#username').val();

        if(username != ''){
           $.ajax({
              url: '/check_username_exists',
              type: 'post',
              data: {username: username},
              success: function(response){
                    if (response == "true"){
                        $('#uname_response').html("");
                        $('#button').removeAttr('disabled');
                    }else{
                        $('#uname_response').html("User does not exist").css({'color':'red', 'text-align':'right'});
                        $('#button').prop('disabled', true);
                    }
               }
           });
        }else{
           $("#uname_response").html("");
        }
    })
})