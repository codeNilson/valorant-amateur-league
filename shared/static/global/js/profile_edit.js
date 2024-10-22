// button = document.getElementById("editButton");
// form = document.getElementById("editForm");
// playerInfo = document.getElementById("playerInfo");

// button.addEventListener("click", function () {
//     form.classList.toggle("d-none");
//     playerInfo.classList.toggle("d-none");
// });

document.addEventListener("DOMContentLoaded", function () {
    function toggleEditForm() {

        button = document.getElementById("editButton");
        form = document.getElementById("editForm");
        playerInfo = document.getElementById("playerInfo");

        if (button && form && playerInfo) {
            button.addEventListener("click", function () {
                form.classList.toggle("d-none");
                playerInfo.classList.toggle("d-none");
            });
        } else {
            console.error("One or more elements not found.");
        }
    }

    toggleEditForm();
});