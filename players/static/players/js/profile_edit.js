document.addEventListener("DOMContentLoaded", function () {
    function toggleEditForm() {
        const editButton = document.getElementById("editButton");
        const cancelButton = document.getElementById("cancelButton");
        const form = document.getElementById("editForm");
        const playerInfo = document.getElementById("playerInfo");

        if (editButton && form && playerInfo && cancelButton) {
            editButton.addEventListener("click", function () {
                form.classList.toggle("d-none");
                playerInfo.classList.toggle("d-none");
            });

            cancelButton.addEventListener("click", function () {
                form.classList.add("d-none");
                playerInfo.classList.remove("d-none");
            });
        } else {
            console.error("One or more elements not found.");
        }
    }

    toggleEditForm();
});