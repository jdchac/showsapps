//Función para la página de consultas
document.addEventListener("DOMContentLoaded", function () {
    const consulta = document.getElementById("consulta");

    consulta.addEventListener("submit", function (event) {
        event.preventDefault(); 
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const dialogMessage = 'Gracias, ' + name + '! Tu mensaje ha sido enviado. Te contactaremos por el correo ' + email + '.';
        alert(dialogMessage);
        consulta.reset();
    });
});

//Función para la recuperación de contraseña
document.addEventListener("DOMContentLoaded", function () {
    const consulta = document.getElementById("pass-recover");
    consulta.addEventListener("submit", function (event) {
        event.preventDefault();
        const email = document.getElementById("emailrecovery").value;
        const dialogMessage = 'Hemos recibido tu correo. Las instrucciones para recuperar tu usuario o contraseña serán enviadas a la dirección ' + email +'.';
        alert(dialogMessage);
        consulta.reset();
    });
});

//Función para el registro de usuario
document.addEventListener("DOMContentLoaded", function () {
    const consulta = document.getElementById("sign-up");
    consulta.addEventListener("submit", function (event) {
        event.preventDefault(); 
        const email = document.getElementById("signup-email").value;
        const dialogMessage = 'Hemos enviado el enlace de confirmación de usuario a la dirección ' + email +'.';
        alert(dialogMessage);
        consulta.reset();
        window.location.href = 'index.html';
    });
});
