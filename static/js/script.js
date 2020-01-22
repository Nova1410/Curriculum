window.addEventListener("load", inicio);

// Manejo de formularios
//Expresión regular para validar email
let regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
//llamando inputs y formulario
let email = document.querySelector('#id_email');
let conEmail = document.querySelector('#id_confirmarEmail');
let tipoDocu = document.querySelector('#id_IdTipoDocu');
let idUsuarios = document.querySelector('#id_IdUsuarios');
let usuario = document.querySelector('#id_username');
let inputs = document.querySelectorAll('input');
let contrasena = document.querySelector('#id_password');
let conContrasena = document.querySelector('#id_confirmarPass');
let formulario = document.querySelectorAll('form')[0];
//Validación ConfirmarEmail
conEmail.addEventListener("keyup", (event) => {
    let inputTieneEspacio = 0;
    for (let j = 0; j < conEmail.value.length; j++) {
        if (conEmail.value.charAt(j) == " ") {
            inputTieneEspacio += 1;
        }
    }
    if(inputTieneEspacio > 0){
        conEmail.className = "inputError form-control";
    }else if(inputTieneEspacio == 0){
        conEmail.className = "inputValid form-control";
    }
    if (email.value == conEmail.value) {
        conEmail.className = "inputValid form-control";
        if(inputTieneEspacio > 0){
            conEmail.className = "inputError form-control";
        }else if(inputTieneEspacio == 0){
            conEmail.className = "inputValid form-control";
        }
    } else if (!(email.value == conEmail.value)) {
        conEmail.className = "inputError form-control";
    }
    inputTieneEspacio = 0;
    if (email.value == "" || email.value == null) {
        conEmail.className = "form-control";
    }
});
//Validación Email
email.addEventListener("keyup", (event) => {
    let inputTieneEspacio = 0;
    for (let j = 0; j < email.value.length+1; j++) {
        if (email.value.charAt(j) == " ") {
            inputTieneEspacio += 1;
        }
    }
    if(inputTieneEspacio > 0){
        email.className = "inputError form-control";
    }else if(inputTieneEspacio == 0){
        email.className = "inputValid form-control";
    }
    if (regex.test(email.value)) {
        email.className = "inputValid form-control";
        if(inputTieneEspacio > 0){
            email.className = "inputError form-control";
        }else if(inputTieneEspacio == 0){
            email.className = "inputValid form-control";
        }
    } else {
        email.className = "inputError form-control";
    }
    inputTieneEspacio = 0;
    if (email.value == "" || email.value == null) {
        conEmail.className = "form-control";
    }
});
//Validación Tipo Documento
tipoDocu.addEventListener("change", (event)=>{
    if (tipoDocu.value != 0){
        tipoDocu.className = "inputValid form-control";
    }else{
        tipoDocu.className = "inputError form-control";
    }
});
//Validación de varios inputs
for (let i = 0; i < inputs.length; i++) {
    let inputTieneEspacio = 0;
    //validación de cedula y usuario
    if (inputs[i].id == "id_IdUsuarios" || inputs[i].id == "id_username"){
        inputs[i].addEventListener("keyup", (event) => {
            //validación si un campo tiene espacios
            for (let j = 0; j < inputs[i].value.length; j++) {
                if (inputs[i].value.charAt(j) == " ") {
                    inputTieneEspacio += 1;
                }
            }
            if(inputTieneEspacio > 0){
                inputs[i].className = "inputError form-control";
            }else if(inputTieneEspacio == 0){
                inputs[i].className = "inputValid form-control";
            }
            inputTieneEspacio = 0;
            if (inputs[i].value == "" || inputs[i].value == null){
                inputs[i].className = "form-control";
            }
            //Validación especifica de cedula
            if (inputs[i].id == "id_IdUsuarios"){
                //Expresión regular validar si tiene numeros
                let regexNum = /^\d+$/;
                for (let j = 0; j < inputs[i].value.length; j++) {
                    if(regexNum.test(inputs[i].value)){
                        inputs[i].className = "inputValid form-control";
                    }else{
                        inputs[i].className = "inputError form-control";
                    }
                }
            }
        });
    }else if(inputs[i].id == "id_first_name" || inputs[i].id == "id_last_name" || inputs[i].id == "id_Ocup" || inputs[i].id == "id_Titulo"){
        inputs[i].addEventListener("keyup", (event) => {
            console.log(inputs[i].id);
            if (inputs[i].value.length > 0){
                inputs[i].className = "inputValid form-control";
            }else{
                inputs[i].className = "form-control";
            }   
        });
    }
}
conContrasena.addEventListener("keyup", (event) => {
    let inputTieneEspacio = 0;
    if (contrasena.value == conContrasena.value) {
        conContrasena.className = "inputValid form-control";
    } else if (!(contrasena.value == conContrasena.value)) {
        conContrasena.className = "inputError form-control";
    }
    for (let j = 0; j < conContrasena.value.length; j++) {
        if (conContrasena.value.charAt(j) == " ") {
            inputTieneEspacio += 1;
        }
    }
    if(inputTieneEspacio > 0){
        conContrasena.className = "inputError form-control";
    }else if(inputTieneEspacio == 0){
        conContrasena.className = "inputValid form-control";
    }
    inputTieneEspacio = 0;
    if (contrasena.value == null || contrasena.value == "") {
        conContrasena.className = "form-control";
    }
});
contrasena.addEventListener("keyup", (event) => {
    let inputTieneEspacio = 0;
    for (let j = 0; j < contrasena.value.length; j++) {
        if (contrasena.value.charAt(j) == " ") {
            inputTieneEspacio += 1;
        }
    }
    if(inputTieneEspacio > 0){
        contrasena.className = "inputError form-control";
    }else if(inputTieneEspacio == 0){
        contrasena.className = "inputValid form-control";
    }
    inputTieneEspacio = 0;
    if (contrasena.value == null || contrasena.value == "") {
        conContrasena.className = "form-control";
    }
});

formulario.addEventListener("submit", (event) => {
    if (!email.value == conEmail.value) {
        conEmail.className = "inputError form-control";
        event.preventDefault();
    }
    if (!contrasena.value == conContrasena.value) {
        contrasena.className = "inputError form-control";
        event.preventDefault();
    }
});

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