$(document).ready(function () {
    $(".submit").click(function () {
        var location = $('destination').val();
        $(".home").hide(1000);
        $("body").css('background', '#cccccc');
    });
});