
function uploadFile(){
    // console.log($('#course_number').val())
    // console.log($('#course_number').html)
    // console.log($('#course_number').innerText)
    // console.log($('#course_number').innerHTML)
    // console.log(document.getElementById("course_number").innerText)

    var form_data = new FormData();
    form_data.append('input_file', $('#input_file').get(0).files[0]);
    form_data.append('course_number', document.getElementById("course_number").innerText)

    $.ajax({
                url:'/note/upload_file/',
                type:'POST',
                data: form_data,
                processData: false,  // tell jquery not to process the data
                contentType: false, // tell jquery not to set contentType
                success: function(data) {
                    $('#exampleModal').modal('hide');
                    $('#note-list').append(data);
                    console.log($('#exampleModal').html)
                }
            }); // end ajax

    // var input_file = $('#input_file').get(0).files[0];
    // $.post("/note/upload_file/", {input_file: input_file})
    //   .done(function(data) {
    //
    //   });
}


$(document).ready(function () {
  console.log("Document Ready")
  // Add event-handlers
  $("#upload").click(function (e) {
      e.preventDefault();
      uploadFile();
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
