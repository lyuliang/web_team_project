$(document).ready(function () {
    var folder = "./media/textNote/"
    $("#submit").click(function (e) {
        // var note=CKEDITOR.instances.note.document.getBody().getText();//get plaintext without format of the content
        var note=CKEDITOR.instances.note.getData();//get text content with format(<p>..)
        console.log(note);
        // alert(note);
        var format,filename;
        // title = prompt("please input the title of the note");
        // filename = prompt("please input the filename");
        var input =  document.getElementById("input");
        input.style.display ="";
        input.style.zIndex = 1;
        $("#cancel").click(function(e) {
        input.style.display ="none";
        })

        $("#submit2").click(function (e) {
            //user = $("#username").val();
            filename = $("#filename").val();
            format=$("#format").val();
            var type=$("#type").val();
            input.style.display ="none";
            save(format,filename,note,type);//save file locally
        })


    });

    function save(format,filename,note,type){
     var file=filename+format;
     var filePath = folder;
     var fileinfo=note;
    var course=document.getElementById("course_number").innerText;
    console.log(course)
       $.get("/note/upload_note/",
           {
               filePath:filePath,
               fileinfo:fileinfo,
               filename:file,
               course_number:course,
               type:type
           },
           function (data) {
           alert("success!");
           location.reload();
           }
           );
    /*filesaver.js*/
     //    var blob = new Blob([fileinfo], {type: "text/plain;charset=utf-8"});//out_put_string为需要保存到文件的字符串内容
     //    saveAs(blob, filePath);//filename.php为保存的文件名
    }


});