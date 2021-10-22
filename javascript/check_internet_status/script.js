const status = document.querySelector(".status");

let online = () => {
    status.innerText = "Connection Available";
    status.style.backgroundColor = "rgb(25, 109, 0)";
};

let offline = () => {
    status.innerText = "No Connection";
    status.style.backgroundColor = "#E02401";
};

/* "window.navigator.online" returns the online status of the browser.
    The property returns a boolean value, with 'true' meaning online
    and 'false meaning offline. */

if (window.navigator.onLine) {
    online();
} else {
    offline();
}

window.addEventListener("online", online);
window.addEventListener("offline", offline);