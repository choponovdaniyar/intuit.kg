function findAll(node, elemSelector){
    let nodes = $(node).find(elemSelector);
    if (nodes.length == 0){
        let childs = $(node).children();
        for(let x = 0; x < childs.length; ++x){
            res = findAll(childs[x], elemSelector);
            if (res.length > 0)
                return res;
        }
    }
    return nodes;
}

class Accardion{
    constructor(title, nav, parent, icon="nav-title__icon"){
        this.title = title
        this.parent = parent
        this.nav = nav;
        this.icon = icon;
        this.mobile_max_size = 768;
    }



    accardionEffect(ParentJq){
        if( $(window).width() > this.mobile_max_size)
            return null;
            
        let navs = findAll(ParentJq, `.${this.nav}`);
        let title = findAll(ParentJq, `.${this.title}`);    
        let icon = $(title[0]).find(`.${this.icon}`);
        icon.toggleClass(`${this.icon}_active`);
        
        navs.slideToggle(200);
    }
}

navbarAccardion = new Accardion(
    title = "footer__nav-title",
    nav = "footer__nav",
    parent = "footer__navbar",
)

$(`.${navbarAccardion.parent}`).on("click", function(){
    navbarAccardion.accardionEffect(
        ParentJq = this
    );
});

facultiesAccardion = new Accardion(
    title = "footer__nav-title",
    nav = "footer__faculty",
    parent = "footer__faculties",
)
$(`.${facultiesAccardion.parent}`).on("click", function(){
    navbarAccardion.accardionEffect(
        ParentJq = this
    );
});


