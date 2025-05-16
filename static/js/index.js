$(document).ready(function () {

    let lastScroll = $(window).scrollTop();
    if (window.innerWidth < 993) {
        $("#header  #_header_links_wrapper .link_wrapper").addClass('_toggle_header')
    }
    $("._toggle_header").click(function () {
        $("._toggle_header").toggleClass('active')
        $('body').toggleClass('active_body')
        $('#_header_links_wrapper').toggleClass('active')
        $('.header_bg').toggleClass('active')
    })
    $("#_header_links_wrapper .link_wrapper .link").click(function () {
        $("#_header_links_wrapper .link_wrapper .link").removeClass('active')
        $(this).addClass('active')
    })
    $(window).resize(function () {
        if (window.innerWidth < 993) {
            $("#header  #_header_links_wrapper .link_wrapper").addClass('_toggle_header')
        } else {
            $("#header  #_header_links_wrapper .link_wrapper").removeClass('_toggle_header')
        }
    })
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        if (scroll > 10) {
            $("#header").css("background", "black");
        } else {
            $("#header").css("background", "transparent");
        }

        if(scroll > lastScroll) {
            $("#header").css("top", "-110px");
        }
        else {
            $("#header").css("top", "0");
        }

        lastScroll = scroll;


    })

})