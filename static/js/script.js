// Change navbar background when scrolling

$(window).scroll(function () {
    $('nav').toggleClass('scrolled', $(this).scrollTop() > 250);
});