$('select').formSelect();
$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.overflow').css({"overflow-y": "auto"})
    $(".datepicker").datepicker({
        format: "yyyy-mm-dd"
    });
});
