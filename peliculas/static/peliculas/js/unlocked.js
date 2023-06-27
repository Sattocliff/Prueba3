const apiKey = "aa6198b7310ee925239609faf353fb24";
const apiUrl = "http://api.weatherunlocked.com/api/current/";

function obtenerClima(ciudad) {
  const url = `${apiUrl}${ciudad}?app_id=${apiKey}`;
  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // Aquí puedes hacer lo que quieras con los datos obtenidos
    })
    .catch(error => {
      console.error(error);
      // Manejo de errores
    });
}

// Llamada de ejemplo
obtenerClima("Buenos Aires, Argentina");
