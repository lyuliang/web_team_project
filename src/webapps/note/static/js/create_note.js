$(document).ready(function () {
    $("#submit").click(function (e) {
        // var note=CKEDITOR.instances.note.document.getBody().getText();//get plaintext without format of the content
        var note=CKEDITOR.instances.note.getData();//get text content with format(<p>..)
        console.log(note);
        alert(note);


    });

});