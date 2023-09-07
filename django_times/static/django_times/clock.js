/**
 * Función Clock: Obtiene la hora actual formateada de acuerdo a opciones específicas.
 * @returns {string} La hora actual formateada con AM o PM.
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
    var timeString = date.toLocaleTimeString(undefined, options);
    var hours = date.getHours();

    // Agregar "AM" o "PM" según corresponda
    var ampm = hours >= 12 ? 'p. m.' : 'a. m.';
    timeString = timeString + ' ' + ampm;

    return timeString;
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
