$(document).ready(function(){

    $('.masonry').masonry({
      // options...
      gutterWidth: 10,
      isFitWidth: true,
      isResizable: true,
      isAnimated: !Modernizr.csstransitions,
      animationOptions: {
        duration: 750,
        easing: 'easeOutQuart',
        queue: false
      }
    });

    $('#options').toggle

});

setTimeout(function(){
$('#options').animate({
                height: '25'
            }, 300,'easeInBack');
$('#options img').delay(400).fadeIn(300);
},2000);

options = false;

$('#options').click(function(){
    if(!options) {
        $('.masonry').animate({marginTop:'60'},150,'easeInCubic');
        $(this).animate({paddingTop:'25'}, 150,'easeInCubic');
        $('#optionsBar').animate({height:'50'},150,'easeInCubic');
        options = true;
    }
    else {
        $(this).animate({
          paddingTop:'0'
        }, 150,function(){
            $('#optionsBar').animate({height:'0'},150);
            $('.masonry').animate({marginTop:'0'},250);
        });
        options = false;        
    }
});

/*
$(function() {

    var b = $('#box');
    b.css({opacity:0});

    $(window).scroll(function() {
        if ($(this).scrollTop() > 200) {
            b.stop().css({
                display: 'block'
            }).animate({
                opacity: 1,
                'top': '30'
            }, 700, 'easeOutBounce');
        } else {
            b.stop().animate({
                opacity: 0
            }, 150, function() {
                $(this).css({
                    display: 'none',
                    top: '0'
                });
            });
        }
    });

    b.click(function() {
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });

});
*/
