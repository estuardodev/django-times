/**
 * Función Clock: Obtiene la hora actual formateada de acuerdo a opciones específicas.
 * @returns {string} La hora actual formateada.
 */
function Clock() {
    var date = new Date();
    var options = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
    };
    return date.toLocaleTimeString(undefined, options);
}

/**
 * Función UpdateTime: Actualiza el contenido del elemento HTML con el ID "currentDate" con la hora actual.
 */
function UpdateTime() {
    var currentDateElement = document.getElementById("currentDate");
    if (currentDateElement) {
        currentDateElement.innerHTML = Clock();
    }
}

// Se actualiza cada segundo utilizando la función UpdateTime
setInterval(UpdateTime, 1000);
