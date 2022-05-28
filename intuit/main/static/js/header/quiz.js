class Quiz {
    constructor(){
        this.btn = ".quiz__button";
        this.startDiv = ".quiz__start";
        this.itemsDiv = ".quiz__items";
        this.itemDiv = ".quiz__item";
        this.inputsDiv = "form";
        this.quitionDiv = ".quiz__quition"; 
        this.quitionIconDiv = ".quiz__quition-left"       
        
        this.currentItem = null;
        this.currentInput = null;
    }

    toggleQuition(quition){
        if($(quition).text() == "Отправить"){
            let inputs = $(".quiz input");
            let len = inputs.length;
            
            inputs[len - 4].value = inputs[0].value;
            inputs[len - 3].value = inputs[1].value;
            inputs[len - 2].value = inputs[2].value;

            this.currentItem = null;
            this.currentInput = null;            
            
            $(".quiz form button").click();
            return 0;
        }
        if (this.currentItem == null){
            this.currentItem = $(this.itemsDiv).children()[0];
            this.currentInput = $(this.inputsDiv).children()[0];
        } else {
            if(this.currentItem[0] == $(this.itemDiv).last()[0]){
                let inputs = $(".quiz__form-input");
                for(let x = 0; x < inputs.length; ++x){
                    $(this.currentInput).attr("value", inputs[x].value);
                    this.currentInput = $(this.currentInput).next();    
                }
                $(".quiz form button").click()
            }

            $(this.currentInput).attr("value", $(quition).text().trim());

            this.currentInput = $(this.currentInput).next();
            this.currentItem = $(this.currentItem).next();
        }
        
        this.toHidden(this.itemDiv)
        this.toVissible(this.currentItem);

        return this.currentItem == $(this.itemsDiv).children()[0];
    }

    toHidden(Selector){
        $(Selector).css({
            "display": "none"
        }); 
    }
    
    toVissible(Selector, display = "block"){
        
        $(Selector).css({
            "display": display
        });
        
       }
}

let quiz = new Quiz()
   

$(quiz.quitionDiv).on("click", function(){
    quiz.toggleQuition(this)
})
$(quiz.quitionIconDiv).on("click", function(){
    quiz.toggleQuition(this)
})

$(quiz.btn).on("click", function(){
    if(quiz.toggleQuition(this)){
        quiz.toHidden(quiz.startDiv);
    } else {
        quiz.toVissible(quiz.startDiv);
        quiz.toHidden(quiz.itemDiv); 
    }
});  