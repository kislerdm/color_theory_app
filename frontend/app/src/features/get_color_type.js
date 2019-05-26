import React from 'react'
import ReactDOM from 'react-dom'
import "./jscolor.js"
var axios = require('axios')

// get button
var fire = document.getElementById("input_apply");
// get color
var col = document.getElementById("color_value")

var requestor = axios.create({
  baseURL: "api_url"
});

if (fire) {
  fire.addEventListener("click", function() {

  requestor.get('/type/hex', {
      params: {
        hexcode: col.value
      }
    })
    .then(function(response) {
      var type = 'Warm';
      if (response.data.data.is_warm === 0) {
        type = 'Cool'
      }

      const color_type = (
        <div>
          <label htmlFor="output" id="output_label">Color Type:</label>
          <output name="color_type" id="output"> {type} </output>
        </div>
      );
      ReactDOM.render(color_type, document.getElementById("color_type"));
    })
    .catch(function(error) {
      console.log(error);
    });
}, false);
};
