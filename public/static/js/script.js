
$(document).ready(async function() {   

    const response = await fetch("static/auxiliary/profiles.json");
    const profiles = await response.json();

    $('#select_2').empty();
        for (const profile of profiles) {
          if (profile.Type == 'American'){
            $('#select_2').append($('<option>', {
              value: profile.Name,
              text: profile.Name,
            }));
          }
        }

    $('#select_1').on('change', function() {
        var selectedCountry = $(this).val();
        if (selectedCountry == 1) {
          console.log(selectedCountry)
          $('#select_2').empty();
          for (const profile of profiles) {
            if (profile.Type == 'American'){
              $('#select_2').append($('<option>', {
                value: profile.Name,
                text: profile.Name,
              }));
            }
          }
        } 
        if (selectedCountry == 2) {
          console.log(selectedCountry)
          $('#select_2').empty();
          for (const profile of profiles) {
            if (profile.Type == 'Euro'){
              $('#select_2').append($('<option>', {
                value: profile.Name,
                text: profile.Name,
              }));
            }
          }
        } 
      });
  });