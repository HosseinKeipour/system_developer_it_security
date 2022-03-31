// Show and Hide events
// Method 1
$(document).ready(function(){
    $("#hide").click(function(){
        $("#div1").hide();
        //$("#id1").hide(); // access by id
        //$(".test").hide(); // access by class name
    });

    $("#show").click(function(){
        $("#div1").show();
    });
});
/* Method 2
$(function(){
    //.........
}); */

// Jquary Fade fadeIn(), fadeOut(), fadeToggle(), fadeTo()

$(document).ready(function(){
    $("#fade1").click(function(){
        $("#p2").fadeOut(1000); 
    
    $("#fade2").click(function(){
        $("#p2").fadeIn(1000); 
    });
    });
});

// Jquary slide down vs slide toggle

// $(document).ready(function(){
//     $("#slide").click(function()
//     {
//         $(".p1").slideDown("slow");
//     });
// });

$(document).ready(function(){
    $("#slide").click(function()
    {
        $(".p1").slideToggle("slow");
    });
});

// Jquary Animate

$(document).ready(function(){
    $("#a1").click(function(){
        $("#animate").animate({left:"500px"});
    });
});