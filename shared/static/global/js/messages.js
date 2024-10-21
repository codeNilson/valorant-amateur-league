setTimeout(function () {
    let alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        let bsAlert = new bootstrap.Alert(alert);
        alert.classList.remove('show');
        alert.classList.add('fade');
        setTimeout(function () {
            bsAlert.close();
        }, 150);
    });
}, 3000);