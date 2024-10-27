document.addEventListener('DOMContentLoaded', function () {

    var alerts = document.querySelectorAll('.alert');

    function adjustAlertPositions() {

        alerts.forEach(function (alert, index) {
            if (index > 0) {
                const bottomMargin = 125 * index;
                alert.style.bottom = bottomMargin + 'px';
            }
        });
    };

    adjustAlertPositions();

    setTimeout(function () {
        alerts.forEach(function (alert) {

            let bsAlert = new bootstrap.Alert(alert);
            setTimeout(function () {
                bsAlert.close();
            }, 150);
        });
    }, 4000);
});