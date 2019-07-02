/* Función de inicio */
window.addEventListener("load",inicio);

function inicio(){
    
    deshabilitarCampos();
    deshabilitarBotones();

    document.getElementById("BtnEditarP").addEventListener("click",enviarDatosB,false);
    document.getElementById("CancelarDatosB").addEventListener("click",deshabilitarDatosB,false);
    document.getElementById("BtnEditarH").addEventListener("click",habilitarCamposDatosH,false);
    document.getElementById("CancelarDatosH").addEventListener("click",deshabilitarCamposDatosH,false);

    
}

/* Funciones generales */

function deshabilitarCampos(){
    let camposB = document.getElementsByClassName("camposB");
    for(let i = 0;i<camposB.length;i++){
        camposB[i].disabled = true;
    }
    let camposH = document.getElementsByClassName("camposH");
    for(let i = 0;i<camposH.length;i++){
        camposH[i].disabled = true;
    }
}

function deshabilitarBotones(){
    document.getElementById("EnviarDatosB").disabled = true;
    document.getElementById("CancelarDatosB").disabled = true;
    deshabilitarIcons();
    deshabilitarBotonesH();

}

/* Funciones de los datos básicos */

function habilitarCamposDatosB(){
    
    let numDoc = document.getElementById("NumDoc");
    numDoc.disabled = false;
    let camposB = document.getElementsByClassName("camposB");
    for(let i = 0;i<camposB.length;i++){
        camposB[i].disabled = false;
    }
    document.getElementById("EnviarDatosB").disabled = false;
    document.getElementById("CancelarDatosB").disabled = false;
    document.getElementById("Datos-tab").click();
    numDoc.focus();
}

function deshabilitarDatosB(){
    let camposB = document.getElementsByClassName("camposB");
    for(let i = 0;i<camposB.length;i++){
        camposB[i].disabled = true;
    }
    document.getElementById("EnviarDatosB").disabled = true;
    document.getElementById("CancelarDatosB").disabled = true;
}

function enviarDatosB(){
    habilitarCamposDatosB();
}

/* Funciones de la hoja de vida */

function deshabilitarIcons(){
    let icons = document.getElementsByClassName("iconTablas");
    for(let i = 0;i<icons.length;i++){
        icons[i].disabled = true;
    }
}

function habilitarIcons(){
    let icons = document.getElementsByClassName("iconTablas");
    for(let i = 0;i<icons.length;i++){
        icons[i].disabled = false;
    }
}



function deshabilitarBotonesH(){
    let btnsAñadir = document.getElementsByClassName("btnsAñadir");
    for(let i = 0;i<btnsAñadir.length;i++){
        btnsAñadir[i].disabled = true;
    }
    document.getElementById("EnviarDatosH").disabled = true;
    document.getElementById("CancelarDatosH").disabled = true;
}

function habilitarBotonesH(){
    let btnsAñadir = document.getElementsByClassName("btnsAñadir");
    for(let i = 0;i<btnsAñadir.length;i++){
        btnsAñadir[i].disabled = false;
    }
    document.getElementById("EnviarDatosH").disabled = false;
    document.getElementById("CancelarDatosH").disabled = false;
}





function habilitarCamposDatosH(){
    let nomH = document.getElementById("NomH");
    nomH.disabled = false;
    let camposH = document.getElementsByClassName("camposH");
    for(let i = 0;i<camposH.length;i++){
        camposH[i].disabled = false;
    }
    habilitarBotonesH();
    habilitarIcons();
    document.getElementById("Hoja-tab").click();
    document.getElementById("BtnCollapseDatos").click();
    nomH.focus();
}

function deshabilitarCamposDatosH(){
    let camposH = document.getElementsByClassName("camposH");
    for(let i = 0;i<camposH.length;i++){
        camposH[i].disabled = true;
    }
    deshabilitarIcons();
    deshabilitarBotonesH();
}

