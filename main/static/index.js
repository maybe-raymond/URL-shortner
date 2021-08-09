// Add a thing that tells people when a link has been added or not 

class Application{
    constructor(){
        this.form = new FormValidation()
        this.urlContainor = new  UrlContainor()
        this.serverUrl = `http://127.0.0.1:5000/shorten`
        this.responseObject={}
    }

    async dataRequest(server, Data){
        let headers = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
            }
        
        let sendRequest = await fetch(server, {
            method:"post",
            headers: headers,
            body: JSON.stringify(Data)
        })
        
        return sendRequest;
    }

    sendData(server, data){
        this.dataRequest(server, data).then(
            response => response.json().then(
                res => {
                    this.responseObject = res
                    this.urlContainor.addLinkElement(this.responseObject["url"])
                }
            )
        ).catch( e => console.log(e))
    }


    buttonOnclickEvent(){
        this.form.button.addEventListener("click", () => {
            if  (this.form.onclickFunc()){
                this.sendData(this.serverUrl, this.form.InputValue)
            }
        })
    }

    makeClickEvent(){
        this.buttonOnclickEvent()
    }
    

    init(){
        this.makeClickEvent();
    }
}




class FormValidation{
    constructor(){
        this.button = document.querySelector("button")
        this.input = document.querySelector("input")
        this.containor = document.querySelector(".input-contantor")
        this.errorIcon  = document.querySelector("#error-icon")
        this.errorMessage = document.querySelector("#error")
        this.ImageUrl = "../static/assets/icon-error.svg"
        this.InputValue =  this.input.value
        this.web = new RegExp("www\.");
        this.dot = new RegExp("\.co");

    }

    onclickFunc(){
        if (this.isURL(this.InputValue)) {
            this.reset();
            return true
        }
            
        this.AddError()
           
    }


    AddError(){
        this.containor.style.border = "solid 1px red"
        this.errorIcon.data = this.ImageUrl
        this.errorMessage.style.color = "red"
    }


    reset(){
        this.containor.style.border = "none"
        this.errorIcon.data = ""
        this.errorMessage.style.color = "transparent"
    }

    
    isURL(str) {
        // do not know how regex works found this solution on stackoverflow
        // Need to understand how this work 
        //i serously i need to learn how this works 
        regex  = /^(?:(?:https?|ftp):\/\/)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:\/\S*)?$/;
        return regex.test(str); 
    }

}


class UrlContainor{
    constructor(){
        this.url = document.querySelector(".url-containor");
        this.AllLinks = {}
        this.display = false
        this.ImageSrc = "../static/assets/copy.png"
        
    }

    onclickEventCopy(element){
        element.addEventListener("click", () => {
            let paragraph = element.querySelector("p");
            let text = paragraph.innerHTML
            navigator.clipboard.writeText(text)
        })
    }

    makeLinkelement(linkData){
        let div = document.createElement("div")
        let p = document.createElement("p");
        let img = document.createElement("img");
        div.className = "links"
        p.innerHTML = linkData;
        img.setAttribute("id", "copy-icon"); 
        img.setAttribute("src", this.ImageSrc);
        div.appendChild(p)
        div.appendChild(img)
        this.url.appendChild(div)
        return div
    }

    addLinkElement(linkData){
        if ( !this.display ){
            this.url.style.display= "flex"
            this.display = true
        }
        let linkElement =  this.makeLinkelement(linkData)
        this.onclickEventCopy(linkElement)

    }
}




function main(){
    "use strict"
    const App = new Application()
    App.init()
}

main()