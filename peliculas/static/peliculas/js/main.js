const API_KEY = "ace74c0c50f96c32f23c643bca2524ff";


async function getLocation() {
  return new Promise((resolve, reject) => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        position => {
          resolve({ latitude: position.coords.latitude, longitude: position.coords.longitude });
        },
        error => {
          reject(error);
        }
      );
    } else {
      reject(new Error("La geolocalización no está soportada por este navegador."));
    }
  });
}


async function getTemperature(latitude, longitude) {
  const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&units=metric&appid=${API_KEY}`);
  const data = await response.json();
  return data.main.temp;
}


getLocation()
  .then(location => {
    return getTemperature(location.latitude, location.longitude);
  })
  .then(temp => {
    
    document.getElementById("temperature").textContent = `${temp}°C`;
  })
  .catch(error => {
    if (error.code === 1) {
      document.getElementById("temperature").textContent = "El permiso de geolocalización ha sido denegado.";
    } else {
      console.error(error);
      document.getElementById("temperature").textContent = "No se ha podido obtener la temperatura.";
    }
  });

$(document).ready(function() {
  $('#formulario').submit(function(event) {
    event.preventDefault();
    if(validacioncita()!= ""){
      swal("Error de Formulario", validacioncita(), "error");
    }else{
      swal("Envio Correceto", "Nos pondremos en contacto con usted", "success");
  }
    
    
  });

  function validacioncita(){
    var html= "";
    var nombreyapellido = $('#txtnombreyapellido').val();
    var telefono = $('#txtNumero').val();
    var email = $('#txtemail').val();
    var ciudad = $('#cbxciudad').val();
    var regNombre = /^[a-zA-Z ]+$/;
    var regTelefono = /^\d{9}$/;
    var regEmail = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;

    if (!regNombre.test(nombreyapellido)) {
      alert('Ingrese un nombre válido');
    }

    if (!regTelefono.test(telefono)) {
      alert('Ingrese un número de teléfono válido');

    }

    if (!regEmail.test(email)) {
      html+="Ingrese un email válido \n";
    }

    if (ciudad == "0") {
      html += "Ingrese una ciudad \n";
    }
    return html;
  }

  

});


function alertita(){
    Swal.fire(
        'Nos pondremos en contacto a la brevedad',
        'Muchas gracias por tu interes en nosotros!',
        'success'
      )
}

