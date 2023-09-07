/**
 * Función Clock12: Obtiene la hora actual en formato de 12 horas.
 * @returns {string} La hora actual en formato de 12 horas.
 */
function Clock12() {
    var date = new Date();
    var options = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
        hour12: true,
    };

    return date.toLocaleTimeString(undefined, options);
}


/**
 * Función UpdateTime: Actualiza el contenido del elemento HTML con el ID "currentDate" con la hora actual.
 */
function UpdateTime() {
    var currentDateElement = document.getElementById("currentDate12");
    if (currentDateElement) {
        currentDateElement.innerHTML = Clock12();
    }
}

// Se actualiza cada segundo utilizando la función UpdateTime
setInterval(UpdateTime, 1000);
