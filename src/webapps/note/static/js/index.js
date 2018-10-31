$(document).ready(function () {
    console.log("success");
    $("#register").click(function() {
        console.log("hhh");
        var obj = document.getElementById("signin")
        obj.innerHTML="Please fill the form";
        var n = "<input type='text' id='username' class='form-control' placeholder='Username' required ></input>";
        var $username = $(n);
        $("#andrew-id").after($username);
        var p = "<input type='password' id='password2' class='form-control' placeholder='Confirm Password' required ></input>";
        var $password2 = $(p);
        $("#inputPassword").after($password2);
        var obj2 = document.getElementById("signinbtn")
        obj2.innerHTML="Register";
        var obj3 = document.getElementById("register")
        obj3.innerHTML="<a href=\'index.html' class=\'register\' id=\'login\'>Log in</a>";

    });

});