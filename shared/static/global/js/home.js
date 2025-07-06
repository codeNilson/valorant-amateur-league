document.addEventListener('DOMContentLoaded', function () {
    const updateButton = document.querySelector("#updateButton");

    updateButton.addEventListener("click", function (event) {
        event.preventDefault();

        const confirmed = confirm("This will update the ranking and send a notification in discord channel. Proceed?");
        if (confirmed) {
            event.target.closest("form").submit();
        }
    });
});
