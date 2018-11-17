$(document).ready(function () {
    var folder = "./media/textNote/"
    $("#submit").click(function (e) {
        var note=CKEDITOR.instances.note.document.getBody().getText();//get plaintext without format of the content
        // var note=CKEDITOR.instances.note.getData();//get text content with format(<p>..)
        console.log(note);
        // alert(note);
        var user,filename;
        // title = prompt("please input the title of the note");
        // filename = prompt("please input the filename");
        var input =  document.getElementById("input");
        input.style.display ="";
        input.style.zIndex = 1;
        $("#submit2").click(function (e) {
            user = $("#username").val();
            filename = $("#filename").val();

            input.style.display ="none";
            //alert(user);

            save(user,filename,note);//save file locally
        })


    });

    function save(username,filename,note){
     var file=username+"-"+filename;
     var filePath = folder+file;
     var fileinfo=note;

       $.get("/note/upload_note/",
           {
               filePath:filePath,
               fileinfo:fileinfo
           },
           function (data) {
           alert("success");
           }
           );
    /*filesaver.js*/
     //    var blob = new Blob([fileinfo], {type: "text/plain;charset=utf-8"});//out_put_string为需要保存到文件的字符串内容
     //    saveAs(blob, filePath);//filename.php为保存的文件名
    }


});