// This example displays a marker at the center of Australia.
// When the user clicks the marker, an info window opens.
function initMap() {
    const canada = { lat: 56.1304, lng: -106.3468 };
    const newfoundland = {lat: 53.1355, lng: -57.6604};
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: canada,
    });
    const contentString =
        '<div id="content">' +
        '<div id="siteNotice">' +
        "</div>" +
        '<h1 id="firstHeading" class="firstHeading">Canada</h1>' +
        '<div id="bodyContent">' +
        "<p><b>Canada</b>, An attempt at digitalizing Essential Healthcare Processes.</p>" +
        "</div>" +
        "</div>";
    const infowindow = new google.maps.InfoWindow({
        content: contentString,
    });
    const marker = new google.maps.Marker({
        position: canada,
        map,
        title: "Canada",
    });
    marker.addListener("click", () => {
        infowindow.open(map, marker);   
    const marker = new google.maps.Marker({
        position: newfoundland,
        map,
        title: "Newfoundland"
    });

    });
}