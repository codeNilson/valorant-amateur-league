button = document.getElementById("editButton");
form = document.getElementById("editForm");
playerInfo = document.getElementById("playerInfo");

button.addEventListener("click", function () {
    form.classList.toggle("d-none");
    playerInfo.classList.toggle("d-none");
});