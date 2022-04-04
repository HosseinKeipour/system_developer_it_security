$(document).ready(function()
{
    $("p").addClass("demo1");
    $("h1").addClass("demo2");
    $("#b1").click(function()
    {
        $("p").toggleClass("demo2");
    });
    $("#b2").click(function()
    {
        alert("the style are"+ $("p").css("background-color")) // access to p 's css property or specific one
        $("p").css("demo1");
    });

    $("#b3").click(function()
    {
        alert("the style are"+ $("p").css("background-color","green")) // access to p 's css property or specific one
        $("p").css("demo1");
    });
});
