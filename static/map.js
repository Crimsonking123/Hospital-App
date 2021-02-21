// This example displays a marker at the center of Australia.
// When the user clicks the marker, an info window opens.
function initMap() {
    const canada = { lat: 56.1304, lng: -106.3468 };
    const newfoundland = {lat: 53.1355, lng: -57.6604 };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: canada,
    });
    fetch('/data').then(function (res) {
        return res.json()
    }).then(function (data) {
        console.log(data);
        const contentString = `
            <div id="content">
                <h1 id="firstHeading" class="firstHeading">${data["title"]}</h1>
                <div id="bodyContent">
                    <p>${data["message"]}</p>
                </div>
            </div>
        `;
        const constantString1 = `
            <div id="content">
                <h1 id="firstHeading" class="firstHeading">Canada</h1>
                <div id="bodyContent">
                    <p>This is an attempt at digitalising essential processes in healthcare</p>
                </div>
            </div>
        `;
        const constantString2 = `
        <div id="content">
            <h1 id="firstHeading" class="firstHeading">Newfoundland</h1>
            <div id="bodyContent">
                <p>Your Location</p>
            </div>
        </div>
    `;
        const infowindow1 = new google.maps.InfoWindow({
            content: constantString1,
        });
        const infowindow2 = new google.maps.InfoWindow({
            content: constantString2,
        })
        const marker = new google.maps.Marker({
            position: canada,
            map,
            title: "Canada",
        });
        marker.addListener("click", () => {
            infowindow1.open(map, marker);   
        });
        const marker1 = new google.maps.Marker({
            position: newfoundland,
            map,
            title: "Newfoundland"
        });
        marker1.addListener("click", () => {
            infowindow2.open(map, marker1);
        });
    }).catch(function (err) {
        console.error(err);
    });
}
