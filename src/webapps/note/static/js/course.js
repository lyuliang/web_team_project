
function uploadFile(){
    var form_data = new FormData();
    form_data.append('input_file', $('#input_file').get(0).files[0]);
    form_data.append('course_number', document.getElementById("course_number").innerText);
    var access = $('#access').val()
    form_data.append('access', access);
    $.ajax({
                url:'/note/upload_file/',
                type:'POST',
                data: form_data,
                processData: false,  // tell jquery not to process the data
                contentType: false, // tell jquery not to set contentType
                success: function(data) {
                    $('#exampleModal').modal('hide');
                    // if(access == "public")
                    //     $('#note-list').append(data);
                    $('#note-list').append(data);
                }
            }); 
}


$(document).ready(function () {
  console.log("Document Ready")
  // Add event-handlers
  $('#showMine').attr('checked',false);
  // Event Listener for checkbox
  $("#showMine").change(function() { 
    var secs = $('section.col-sm-4');
    var name = $('#hiddenusername').val();
      // Uncheck, get all notes
    if(!$(this).is(':checked'))
    {
        for(var i = 0; i < secs.length; i++)
        {
            $(secs[i]).css('display','block');
        }
    }
    // Check, get only my notes
    else{ 
        for(var i = 0; i < secs.length; i++)
        {
            var sec_name = $(secs[i]).find('em').html();
            if(sec_name != name)
            {
                $(secs[i]).css('display','none');
            }
        }
    }
    });
  $("#upload").click(function (e) {
      e.preventDefault();
      uploadFile();
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
