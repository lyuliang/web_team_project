
function joinCourse(){
    var course_name = $("#course_name")
    var course_number = $("#course_number")
    $.post("/note/join_course/", {"name": course_name.val(), "number": course_number.val()})
      .done(function(data) {
          // data contains valid HTML code
          if (data.startsWith('<'))
           {
              $('#exampleModal').modal('hide'); 
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
              // for (var error in data) {
              //     errors.append($(error.html))
              // }
              errors.html(data)
          }
      });
}

function dropdown_courselist() {
    var courselist = $("#category");
    $.get("/note/dropdown_courselist/")
        .done(function(data) {
            courselist.html('')
            for (var i = 0; i < data.length; i ++) {
                courselist.append($("<option>").attr('value', data[i]))
            }
        });

}

$(document).ready(function () {

  console.log("good")
  // Add event-handlers

  $("#join_course").click(function (e) {
      e.preventDefault();
      joinCourse();
  });
  $('#join-btn').click(function (e) {
    e.preventDefault();
    $('#save-btn').click();
});
  $('.btn-join').click(function (e) {
    e.preventDefault();
    $(this).parent().parent().find('#chosen').val('T');
    $(this).css('background-color','#d9534f');
    $(this).css('color','#ffffff');
    $(this).html('Joined');
    });
   $('.btn-cancel').click(function (e) {
    e.preventDefault();
    $(this).parent().parent().find('#chosen').val('F');
    var join = $(this).parent().parent().find('.btn-join');
    join.css('color','#d9534f');
    join.css('background-color','#ffffff'); 
    join.html('Join In');
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
