// function isElementVisible(elementToBeChecked) {
//     var TopView = $(window).scrollTop();
//     var BotView =  TopView + $(window).height();
//     var TopElement = $(elementToBeChecked).offset().top;
//     var BotElement = TopElement + $(elementToBeChecked).height();

//     return ((BotElement <= BotView) && (TopElement >= TopView));
// }


// $(window).on( "wheel DOMMouseScroll", function() {
    // setTimeout(
    //     function(){
    //         jQuery()
    //         var home = $('#fullpage .home').is(":visible");
    //         var agency = $('.agency').is(":visible");
    //         var expertise = $('.expertise').is(":visible");
    //         var portfolio = $('.portfolio').is(":visible");
        
    //         if (home) {$(".text1").css("color", "white")};
    //         if (agency) {$(".text1").css("color", "black")};
    //         if (expertise) {$(".text1").css("color", "green")};
    //         if (portfolio) {$(".text1").css("color", "red")};
    //         console.log('hi')

    //     }  
    //     , 900
    // );
// });



$(document).ready(function(){
    if($(window).width() > 1023){ 
        $('#fullpage').fullpage()
        }
    else if($(window).width()<1024){
        $('#fullpage').removeAttr('id'); 
    };

    $('.carousel').owlCarousel({
        stagePadding: 0,
        margin: -150,
        loop:true,
        autoplay:true,
        autoplayTimeout:3000,
        autoplayHoverPause: true,
    });
    $('.carousel1').owlCarousel({
        stagePadding: 0,
        margin:-150,
        loop:true,
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause: true,
    });
    
});

