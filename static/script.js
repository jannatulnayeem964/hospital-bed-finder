document.addEventListener("DOMContentLoaded", function () {
    // Add event listener to the submit button
    const submitButton = document.querySelector("input[type='submit']");
    submitButton.addEventListener("click", function () {
        const selectedHospital = document.querySelector("#hospital");
        const bedsNeeded = document.querySelector("input[name='beds']").value;
        const selectedHospitalName = selectedHospital.options[selectedHospital.selectedIndex].text;
        const bedsAvailableElement = document.querySelector(`li:contains('${selectedHospitalName}') span`);
        const bedsAvailable = parseInt(bedsAvailableElement.textContent);

        if (bedsAvailable < bedsNeeded) {
            alert("Not enough beds available.");
            event.preventDefault(); // Prevent form submission
        }
    });
});

// Custom contains function for selecting elements by text
jQuery.expr[':'].contains = function(a, i, m) {
    return jQuery(a).text().indexOf(m[3]) >= 0;
};
