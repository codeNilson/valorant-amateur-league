document.addEventListener('DOMContentLoaded', function () {
    const updateButton = document.querySelector("#updateButton");

    updateButton.addEventListener("click", function (event) {
        event.preventDefault(); // Impede o comportamento padrão inicialmente

        const confirmar = confirm("This will update the ranking and send a message in discord channel. Are you sure?");
        if (confirmar) {
            event.target.closest("form").submit();
        }
    });
});
