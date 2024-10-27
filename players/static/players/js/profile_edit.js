document.addEventListener("DOMContentLoaded", function () {
    function toggleEditForm() {
        const editButtons = document.querySelectorAll(".editButton");
        const cancelButtons = document.querySelectorAll(".cancelButton");

        editButtons.forEach(editButton => {
            const dataId = editButton.getAttribute("data-id");
            const form = document.querySelector(`.editForm[data-id="${dataId}"]`);
            const playerInfo = document.querySelector(`.playerInfo[data-id="${dataId}"]`);
            const cancelButton = document.querySelector(`.cancelButton[data-id="${dataId}"]`);

            if (form && playerInfo && cancelButton) {
                editButton.addEventListener("click", function () {
                    form.classList.toggle("d-none");
                    playerInfo.classList.toggle("d-none");
                });

                cancelButton.addEventListener("click", function () {
                    form.classList.add("d-none");
                    playerInfo.classList.remove("d-none");
                });
            } else {
                console.error(`Elements with data-id="${dataId}" not found.`);
            }
        });
    }

    toggleEditForm();
});
