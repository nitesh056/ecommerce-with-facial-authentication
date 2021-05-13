function scanFace() {
    $.ajax({
        url: "/u/save-face/",
        type: "GET",
        success: function(resp){
            $("body").append(resp);
            $('#face-capture').modal('show');
        }
    });
}

function authWithFace() {
    $.ajax({
        url: "/u/auth-with-face/" + $('#email').val(),
        type: "POST",
        success: function(resp){
            if (resp == "error while getting email") {
                $("#errorMessage").append(resp);
            } else {
                $("body").append(resp);
                $('#face-auth').modal('show');
            }
            // $("#face-auth").show();
        }
    });
}