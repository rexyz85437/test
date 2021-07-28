var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 25.04, lng: 121.512},
    zoom: 18
    });
}