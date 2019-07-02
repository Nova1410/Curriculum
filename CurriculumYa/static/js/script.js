window.addEventListener("load", inicio);

function inicio(){
    addClases();
}

function addClases(){
    Url = window.location.toString().split('?')[0];
    
    if(Url == "http://127.0.0.1:8000/"){
        UserInput = document.getElementById('id_username');
        $('#id_username').addClass("form-control");//.attr("placeholder","Username:");
        $('#id_password').addClass("form-control");//.attr("placeholder","Password:");
    }
    
}

function limpiarUrl(event){
    var tecla = event.keyCode;
    var Url = window.location
    var split = Url.toString().split('?');

    if(tecla == 116 && split[0] == "http://127.0.0.1:8000/usuario/perfil/update"){
        location.href = "/usuario/perfil/update"
    }

    if(tecla == 116 && split[0] == "http://127.0.0.1:8000/"){
        location.href = "/"
    }
}

window.onkeydown = limpiarUrl;