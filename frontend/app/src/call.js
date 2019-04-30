import "./jscolor.js"

var axios = require('axios')

// get button
var fire = document.getElementById("input_apply");
// get color
var col = document.getElementById("color_value")

var requestor = axios.create({
  baseURL: "https://www.dkisler.de/api/color_theory_app/backend"
});

if (fire) {
  fire.addEventListener("click", function() {

    let out = document.getElementById("output");

    requestor.get('/hex', {
        params: {
          hexcode: col.value
        }
      })
      .then(function(response) {
        var type = 'Warm';
        if (response.data.data.is_warm === 0) {
          type = 'Cool'
        }

        out.innerHTML = type;

      })
      .catch(function(error) {
        console.log(error);
      });

  }, false);
};
