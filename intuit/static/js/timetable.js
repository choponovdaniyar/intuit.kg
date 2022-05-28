$(".timetable__item").on("click", function(){
    let content = `e${$(this).attr("id")}`;

    $(".timetable__content").css({"display": "none"}) 
    $(`#${content}`).css({"display": "grid"}) 
    console.log()
});
$(".timetable__content").css({"display": "none"}) 