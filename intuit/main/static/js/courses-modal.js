
class CoursesModal{
    constructor(){
        this.modalButton = ".courses-modal__button";
        this.modals = document.querySelectorAll(this.modalButton);
        
        this.activate = false;


        this.onClickActive();
    }


    onClickActive(){
        // activate modalButtons
        for(let x=0; x < this.modals.length; ++x){

            let modal = this.modals[x].parentElement;
            let button = modal.parentElement;

            this.modals[x].onclick = () =>{
                if (this.activate)
                    modal.style.display = "none";
            }

            button.onclick = () => {
                if (!this.activate)
                    modal.style.display = "flex";
                this.activate = !this.activate;
            }
        }
    }

}

let modal = new CoursesModal();


