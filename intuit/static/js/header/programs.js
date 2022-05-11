let count = 6;
let programs = $(".program");
let valid_programs = programs;


function get_programs(){
    for (let x = 0; x < count;  ++x){
        let pos = valid_programs.length - 1;

        if(pos == -1){
            let button = ".program__button"
            if($(button).css("display") == "flex"){
                $(button).css({
                    "display": "none"
                })
            }
            return 0
        }

        $(valid_programs[pos]).parent().slideToggle(200)
        valid_programs.pop();
    }

}


function programs_vissible(choice){
    valid_programs = Array();

    programs.parent().css({
        "display": "none"
    })
    
    for (let x = 0; x < programs.length; ++x){
        let edu = $($(programs[x]).children()[0]).text();
        let reg = RegExp(choice.toLowerCase());

        if(reg.test(edu.toLowerCase()))
            valid_programs.push(programs[x])
    }

    valid_programs.reverse();

    get_programs();
}


programs_vissible("")


$(".program__button-inner").on("click", function(){
    get_programs()
});


$(".programs__education").on("click", function(){
    $(".programs__education").removeClass("programs__education_active");
    $(this).toggleClass("programs__education_active");

    programs_vissible( $(this).text() )
})

