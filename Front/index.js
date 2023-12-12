const navMenu = document.querySelector("#navMenu");
const abrir = document.querySelector("#abrir");
const cerrar = document.querySelector("#cerrar");

abrir.addEventListener("click", () =>{
    navMenu.classList.add("visible");
})

cerrar.addEventListener("click", () =>{
    navMenu.classList.remove("visible");
})