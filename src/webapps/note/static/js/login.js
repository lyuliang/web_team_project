$(document).ready(function () {
    console.log("success");
    $("#register").click(function() {
        console.log("hhh");
        var obj = document.getElementById("signin")
        obj.innerHTML="Please fill the form";
        // Change the URL of sign-in form to register URL
        var form = $('.form-signin')
        form.attr('action','/note/register/')
        var n = "<input type='text' name = 'andrewid' id='andrew-id' class='form-control' placeholder='Andrew id' required ></input>";
        $("#username").after($(n));
        var p = "<input type='password' name = 'pw2' id='password2' class='form-control' placeholder='Confirm Password' required ></input>";
        var $password2 = $(p);
        $("#inputPassword").after($password2);
        var obj2 = document.getElementById("signinbtn")
        obj2.innerHTML="Register";
        // Add a signin link to return to Signin Page
        var obj3 = document.getElementById("register")
        obj3.innerHTML="<a href='' class='register' id='login'> Log in</a>";

    });
    // $("#check-student").focus(function () {
    //     if()
    //      $("#check-prof").attr("checked",false);
    // })

});