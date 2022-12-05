// create a map in the "map" div, set the view to a given place and zoom
var map = L.map('map').setView([48.858190, 2.294470], 16);

// add an OpenStreetMap tile layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// add a marker in the given location, attach some popup content to it and open the popup
L.marker([48.858190, 2.294470]).addTo(map)
    .bindPopup('This is the Eiffel Tower<br> Easily customizable.')
    .openPopup();


// create a map in the "map" div, set the view to a given place and zoom
var map2 = L.map('map2').setView([48.858190, 2.294470], 16);

// add an OpenStreetMap tile layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map2);