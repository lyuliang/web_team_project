
function createCourse(){
    var course_name = $("#course_name")
    var course_number = $("#course_number")
    $.post("/note/create_course/", {name: course_name.val(), number: course_number.val()})
      .done(function(data) {
          if (data.startsWith('<')) {
            $('#exampleModal').modal('hide'); 
            // Add new course to HTML
            var newcourse  = $(data)
            if (newcourse.find('#unselected').val() == 'False'){
                // Delete All Courses, only leave the new added courses
                $('.posts').empty();
                $('.posts').append();
            }
             $('.posts').append(data)
          }
          else {
              var errors = $("#errors");
              console.log(data)
              errors.html(data)
          }
      });
}


$(document).ready(function () {
  console.log("Document Ready")
  // Add event-handlers
  $("#create_course").click(function (e) {
      e.preventDefault();
      createCourse();
  });

  // CSRF set-up copied from Django docs
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
});
