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

function validateForm() {
    var locationInput = document.getElementById("locat");
    if (locationInput.value.trim() === "") {
        alert("Location is required.");
        locationInput.focus();
        return false;
    }

    var quality = document.getElementById("qual");
    if (quality.value == "") {
        alert("Value is required.");
        quality.focus();
        return false;
    }
    return true;
}


function validateReview() {
    var locationInput = document.getElementById("locat");
    if (locationInput.value.trim() === "") {
        alert("Location is required.");
        locationInput.focus();
        return false;
    }

    var quality = document.getElementById("qual");
    if (quality.value === "") {
        alert("Value is required.");
        quality.focus();
        return false;
    }

    var review = document.getElementById("review");
    if (review.value.trim() === "") {
        alert("Review is required.");
        review.focus();
        return false;
    }
    return true;
}

// Add a click event listener to the "Use Current Location" button
const useCurrentLocationButton = document.getElementById("useCurrentLocation");
useCurrentLocationButton.addEventListener("click", getCurrentLocation);
