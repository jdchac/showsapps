//Checkout Roger Waters

document.addEventListener("DOMContentLoaded", function (event) {
    const rogerCheckout = document.getElementById("rogerCheckout");

    rogerCheckout.addEventListener("submit", function (event) {
        event.preventDefault(); 
        var numGeneral = document.getElementById("entradaGeneral").value;
        var numVIP = document.getElementById("entradaVIP").value;
        var numEntradas = numGeneral + numVIP;
        var total = (numGeneral*5000) + (numVIP*10000);

        if (numGeneral==0 && numVIP==0) {
            alert('Elige al menos una (1) entrada para proceder al checkout.');
            return false;
        } else {
            true;
            alert('Total a pagar: $' + total + '.')
            window.location.href = 'checkout.html';

        }  
        var botonCheckout = document.getElementById("total");
        botonCheckout.innerText = 'Total: $' + total;
    });
});
 //Aviso de Checkout
document.addEventListener("DOMContentLoaded", function () {
    const consulta = document.getElementById("payment");

    consulta.addEventListener("submit", function (event) {
        event.preventDefault(); 
        const dialogMessage = 'Operación no disponible temporalmente. Sitio en construcción. Haz click en aceptar para volver al inicio.';
        alert(dialogMessage);
        window.location.href = 'index.html';
    });
});