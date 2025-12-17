document.addEventListener("DOMContentLoaded", function () {
    const unavailableDatesEl = document.getElementById("unavailable-dates");
    const unavailableDates = unavailableDatesEl
        ? JSON.parse(unavailableDatesEl.textContent)
        : [];

    flatpickr("#id_stay-multi_dates", {
        mode: "range",
        dateFormat: "Y-m-d",
        altInput: true,
        altFormat: "F j, Y",
        minDate: "today",
        disable: unavailableDates,
    });
});
