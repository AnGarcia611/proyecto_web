$(document).ready(function() {
    $('#boton_1').on('click', async function() {

      const select2Value = $(document.getElementById('select_2')).val();
      const select3Value = $(document.getElementById('select_3')).val();
      const select4Value = $(document.getElementById('select_4')).val();
      const select5Value = $(document.getElementById('select_5')).val();
      var fit = false

      if (select5Value == "Rectangular") {
        fit = true;
    } if (select5Value == "Cuadrado"){
        fit = false;
    }

    const headers = {
        select2: select2Value,
        select3: select3Value,
        select4: select4Value,
        select5: fit,
      };

      // Realiza una solicitud a la API
      const url = `/update?profile=${select2Value}&bolt=${select3Value}&n_bolts=${select4Value}&fit=${fit}`;
      const response = await fetch(url);

      // Obtiene la imagen como un objeto Blob
      const imageBlob = await response.blob();
  
      // Crea un objeto FileReader para leer el objeto Blob
      const reader = new FileReader();
  
      // Agrega un evento onload al objeto FileReader para manejar la carga de la imagen
      reader.onload = async function() {
        // Obtiene la imagen codificada en base64
        const base64Image = await reader.result;
        console.log(base64Image)
        // Actualiza el HTML con la imagen codificada en base64
        $('#imagen').attr('src', base64Image);
      };
  
      // Lee el objeto Blob
      reader.readAsDataURL(imageBlob);
    });


  });

document.getElementById('boton_2').addEventListener('click', function() {
    const select2Value = $(document.getElementById('select_2')).val();
    const select3Value = $(document.getElementById('select_3')).val();
    const select4Value = $(document.getElementById('select_4')).val();
    const select5Value = $(document.getElementById('select_5')).val();
    var fit = false

    if (select5Value == "Rectangular") {
      fit = true;
    }
    
    if (select5Value == "Cuadrado"){
      fit = false;
    }

    const headers = {
        select2: select2Value,
        select3: select3Value,
        select4: select4Value,
        select5: fit,
      };

    // Realiza una solicitud a la API
    const url = `/dxf?profile=${select2Value}&bolt=${select3Value}&n_bolts=${select4Value}&fit=${fit}`;
  
    
    n.href = url;
  });