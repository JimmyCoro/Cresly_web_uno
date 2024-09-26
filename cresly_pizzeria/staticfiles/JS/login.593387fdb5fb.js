$(document).ready(function () {
    $('#loginForm').on('submit', function (e) {
        e.preventDefault();  // Prevenir el envío normal del formulario
        
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),
            dataType: 'json',
            success: function (response) {
                if (response.success) {
                    Swal.fire({
                        title: 'Éxito',
                        text: response.message,
                        icon: 'success',
                        confirmButtonText: 'Continuar'
                    }).then((result) => {
                        if (result.isConfirmed) {
                            location.reload();  // Recargar la página después del inicio de sesión
                        }
                    });
                }
            },
            error: function (xhr) {
                var errors = xhr.responseJSON.errors;
                var errorText = '';
                for (var field in errors) {
                    errorText += errors[field].join('<br>') + '<br>';
                }
                $('#login-errors').html(errorText);  // Mostrar los errores en el div correspondiente
            }
        });
    });

    $('#registerForm').on('submit', function (e) {
        e.preventDefault();  // Prevenir el envío normal del formulario

        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),
            dataType: 'json',
            success: function (response) {
                if (response.success) {
                    Swal.fire({
                        title: 'Éxito',
                        text: response.message,
                        icon: 'success',
                        confirmButtonText: 'Continuar'
                    }).then((result) => {
                        if (result.isConfirmed) {
                            location.reload();  // Recargar la página después del registro
                        }
                    });
                }
            },
            error: function (xhr) {
                var errors = xhr.responseJSON.errors;
                var errorText = '';
                for (var field in errors) {
                    errorText += errors[field].join('<br>') + '<br>';
                }
                $('#register-errors').html(errorText);  // Mostrar los errores en el div correspondiente
            }
        });
    });
});
