
const _api_key = document.getElementById('geolocation-data')
  .getAttribute('data-api-key');
const _api_domain = document.getElementById('geolocation-data')
  .getAttribute('data-api-domain');

function checkLocation(infoText) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                var request = new XMLHttpRequest();

                var url = _api_domain
                    +'?key='+_api_key
                    +'&lat='+position.coords.latitude+'&lon='+position.coords.longitude
                    +'&format=json&postaladdress=1&normalizeaddress=1&zoom=18';

                request.open('GET', url, true);
                request.onreadystatechange = function(){
                    if (request.readyState == 4 && request.status == 200){
                        var data = JSON.parse(request.responseText);
                        displayLocation(data, infoText);
                    }
                    else {
                        handleLocationError(true, infoText);
                    }
                };
                request.send();
            },
            () => { handleLocationError(true, infoText); }
        );
    }
    else {
        handleLocationError(false, infoText);
    }
}

function displayLocation(data, infoText) {
    // road suburb city country | city_district locality state_district
    var address = data.address;
    // var name = address.road ? address.road+', ' : '';
    var name = address.city ? address.city+', ' : '';
    name += address.country ? address.country : '';
    infoText.innerHTML = name;

    locationInput = document.getElementById('id_location');
    locationInput.value = name;

    button = document.getElementById('location-button');
    button.style.display = 'none';
}

function handleLocationError(browserHasGeolocation, infoText) {
    infoText.innerHTML = browserHasGeolocation
        ? 'Error: The Geolocation service failed.'
        : 'Error: Your browser doesn\'t support geolocation.';
}

window.onload = () => {
    var infoText = document.getElementById('location-text');
    var button = document.getElementById('location-button');
    if (button)
        button.addEventListener('click', () => {checkLocation(infoText)});
};
