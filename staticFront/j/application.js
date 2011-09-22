$(document).ready(function(){
    $.get("twitter_trend", function(data) {
        trends = $("#trends").html();
        $("#trends").html(trends + data);
    });
  
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

$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
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
