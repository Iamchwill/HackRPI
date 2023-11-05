// Function to update the location input with the current location
function getCurrentLocation() {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            const locationInput = document.getElementById("locat");
            locationInput.value = `${latitude}, ${longitude}`;
        }, function (error) {
            console.error("Error getting current location:", error);
        });
    } else {
        console.error("Geolocation not supported by the browser.");
    }
}

// Add a click event listener to the "Use Current Location" button
const useCurrentLocationButton = document.getElementById("useCurrentLocation");
useCurrentLocationButton.addEventListener("click", getCurrentLocation);
