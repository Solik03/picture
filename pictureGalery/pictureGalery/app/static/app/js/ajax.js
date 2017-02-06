        $("#username").focus(function(){
        $(this).css("background-color", "#00ff00");
    });
        $("#username").focusout(function(){
            var json ={
                username:  $("#username").val() 
        };
        var data_json = JSON.stringify(json);
        $.ajax({
        type: 'POST',
        url: "register/process",
        dataType: "json",
        data:data_json,
        success: function (obj) {
            if (obj.free) {
                $("#username").css("background-color", "#ffffff");
                $("#register-submit").show();
            } else{
                $("#register-submit").hide();
                $("#username").css("background-color", "#ff0000");
            }
        },

    });
});