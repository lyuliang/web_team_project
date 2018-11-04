
function joinCourse(){
    var course_name = $("#course_name")
    var course_number = $("#course_number")
    $.post("/note/join_course/", {"name": course_name.val(), "number": course_number.val()})
      .done(function(data) {
          // data contains valid HTML code
          if (data.startsWith('<'))
           {//data==""说明views中return HttpResponse(""),即没有error)
              //$('#cancel').click()
              $('#exampleModal').modal('hide'); 
              $('.posts').append(data)
              // getUpdates(); //待实现
          }
          else {
              // alert(data); //course name或number invalid，显示错误信息
              var errors = $("#errors");
              console.log(data)
              // for (var error in data) {
              //     errors.append($(error.html))
              // }
              errors.html(data)
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

  // 开始时显示一遍课程列表
  // initialCourseList(); //待实现

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
