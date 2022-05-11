'use strict';

class Burger{
    constructor() {
        this.menuTrigger = $('#menu-trigger');
        this.toggleMenu();
    }

    toggleMenu() {
        var _this = this;
        this.menuTrigger.on('click', function () {
            alert('asd')
            _this.menuTrigger.toggleClass('is-open');
            _this.menu.toggleClass('is-open');
        });
    };
}


let burger = new Burger();

$('.burger__btn').on("click", function(){
    $(this).toggleClass('is-open');
    $("main").slideToggle(200);
    $(".footer__faculties").slideToggle(200);
    $(".footer__educations").slideToggle(200);
    $(".footer__aside").slideToggle(200);

})

