class FacultyList{
    constructor(){
        this.colors = ["green", "blue", "yellow", "violet", "red"];
        this.className = null;
        this.classPrefix = "faculities__item" 
    }

    getRandomInt() {
        let min = 0;
        let max = this.colors.length - 1;
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    getClassName(){
        let x = this.getRandomInt();
        console.log(x);
        if(`${this.classPrefix}_${this.colors[x]}` == this.className)
            return this.getClassName();
        this.className = `${this.classPrefix}_${this.colors[x]}`;
    }
    

    addClass(obj){
        this.getClassName();
        console.log(this.className)
        $(obj).addClass(this.className);
    }
    removeClass(obj){
        $(obj).removeClass(this.className);
    }
}


let fl = new FacultyList();

$(".faculities__item").on("mouseenter",function(){
    fl.addClass(this);
})
$(".faculities__item").on("mouseleave",function(){
    fl.removeClass(".faculities__item")
})