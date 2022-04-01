$(document).ready(function(){



    $("#b3").click(function(){
        alert(""+"alert");
    });
        
    $("#b4").click(function(){
        alert(""+"alert");
    });

    $("#b5").click(function(){
        $("#p1").text("Hello HTML usinf text()")
    });
    $("#b6").click(function(){
        $("#p1").html("<h1>Hello HTML usinf html()</h1>")
    });
    $("#b7").click(function(){
        $("#i1").val("Hi I am setted by val()")
    });

    //
    $("#b8").click(function(){
        $("p").append("<img src='car.png' height='50px' width='20px'>"); // eg. after all paragraph
    });
    $("#b9").click(function(){
        $("p").remove("<img src='car.png' height='50px' width='20px'>"); // eg. after all paragraph
    });
});