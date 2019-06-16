import React from 'react'
import ReactDOM from 'react-dom'
import "./jscolor.js"

var axios = require('axios')

// get button
var fire = document.getElementById("input_apply");
// get color
var col = document.getElementById("color_value");

var requestor = axios.create({
  baseURL: "api_url"
});

if (fire) {
  fire.addEventListener("click", function() {

  requestor.get('/name/hex', {
      params: {
        hexcode: col.value
      }
    })
    .then(function(response) {
      var name = 'Unknown';
      if (response.data.data.name) {
        name = response.data.data.name
      }

      const color_name = (
        <div>
          <label htmlFor="output_name" id="output_label">Color Name:</label>
          <output name="color_name" id="output_name"> {name} </output>
        </div>
      );
      ReactDOM.render(color_name, document.getElementById("color_name"));
    })
    .catch(function(error) {
      console.log(error);
    });
}, false);
};
