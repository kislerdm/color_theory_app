var axios = require('axios')

// get button
var fire = document.getElementById("input_apply");

var requestor = axios.create({
  baseURL: "https://www.dkisler.de/api/color_theory_app/backend"
});

if (fire) {
  fire.addEventListener("click", function() {
    let r = document.getElementById("input_r").value;
    let g = document.getElementById("input_g").value;
    let b = document.getElementById("input_b").value;
    let out = document.getElementById("output");

    requestor.get('/rgb', {
        params: {
          r: r,
          g: g,
          b: b
        }
      })
      .then(function(response) {
        var type = 'warm';
        if (response.data.data.is_warm === 0) {
          type = 'cool'
        }

        out.innerHTML = type;

      })
      .catch(function(error) {
        console.log(error);
      });

  }, false);
};
