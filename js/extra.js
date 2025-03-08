document.addEventListener("DOMContentLoaded", function () {
    if (window.location.href.includes("local-systems")) {
        document.body.classList.add("url-matched");
    }
});
