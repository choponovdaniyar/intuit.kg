let nav = ".for-enrollee__nav";
$(nav).on("click", function(){
    let active = "for-enrollee__nav_active";
    $(nav).removeClass(active);
    $(this).addClass(active);
    if ($(this).attr("id") == 'employment'){
        $(".for-enrollee__employment").css({
            "display": "block"
        }) 
    } else {
        $(".for-enrollee__employment").css({
            "display": "none"
        })
    }

    if ($(this).attr("id") == 'rule'){
        $(".for-enrollee__rule").css({
            "display": "block"
        }) 
    } else {
        $(".for-enrollee__rule").css({
            "display": "none"
        })
    }
    

   
    if ($(this).attr("id") == 'quitions'){
        $(".for-enrollee__quitions").css({
            "display": "grid"
        }) 
    } else {
        $(".for-enrollee__quitions").css({
            "display": "none"
        })
    }
})

