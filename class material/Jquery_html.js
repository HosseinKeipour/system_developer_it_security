$(document).ready(function(){
    $("#b1").click(function(){
        alert("The text of the <p> element is: "+$("#text").text());
    });
    $("#b2").click(function(){
        alert("The content of the <p> element is: "+$("#text").html());
    });


    $("#b3").click(function(){
        alert("The content of the Form element is " + " " + $("#i1").val());
    });
        
    $("#b4").click(function(){
        alert("The Attributes are " + " " + $("#i1").attr());
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
        $("#d1").remove(); 
    });
    $("#b10").click(function(){
        $("#d1").empty(); 
    });
});