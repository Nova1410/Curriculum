function actualizarIndexElementos(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);

}

function añadirClases() {
    var total = $('#id_' + "experiencias" + '-TOTAL_FORMS').val();
    var deleteCheckbox = $('.checkboxDelete').find(':input').each(function (indice, elemento) {
        $(elemento).attr('id', 'id_form-' + (total - 1) + '-DELETE');
    });
}

function actualizarFilas(fila) {
    var count = 0;
    var forms = $(fila);
    for (var i = 0, formCount = forms.length; i < formCount; i++) {
        if ($(forms.get(i)).find('th').html() != '0') {
            $(forms.get(i)).find('th').html(function () {
                nuevo = count + 1;
                count++;
                return nuevo;
            });
        }
    }
}

function borrarFila(prefix, fila, btn) {
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    var countTotal = parseInt($('#' + prefix + 'Total').val());
    if (total >= 1) {
        if (btn.closest(fila).find('.id-row').children().val() == "") {
            btn.closest(fila).remove();
            var forms = $(fila);
            $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
            countTotal--;
            $('#' + prefix + 'Total').val(countTotal);
            for (var i = 0, formCount = forms.length; i < formCount; i++) {
                $(forms.get(i)).find(':input').each(function () {
                    actualizarIndexElementos(this, prefix, i);
                });

                actualizarFilas(fila)
            }
        } else {
            countTotal--;
            $('#' + prefix + 'Total').val(countTotal);
            btn.closest(fila).addClass('deshabilitar');
            btn.closest(fila).find('th').html('0');
            actualizarFilas(fila);
        }

    }

}


function checkear(btn, fila) {
    btn.closest(fila).find('.checkboxDelete').children().attr('checked', true)
    //$('#id_'+ prefix +'-'+ (num-1) +'-DELETE').prop('checked',true);
    return false;
}

function añadirPrimeraFila(prefix, total) {
    idUser = $('#id_datospersona-IdUsuarios').val()
    switch (prefix) {
        case 'educaciones':
            $('#EduContent').html(function () {
                var nuevo = '<input type="hidden" name="educaciones-TOTAL_FORMS" value="1" id="id_educaciones-TOTAL_FORMS"><input type="hidden" name="educaciones-INITIAL_FORMS" value="' + total + '" id="id_educaciones-INITIAL_FORMS"><input type="hidden" name="educaciones-MIN_NUM_FORMS" value="0" id="id_educaciones-MIN_NUM_FORMS"><input type="hidden" name="educaciones-MAX_NUM_FORMS" value="1000" id="id_educaciones-MAX_NUM_FORMS">' +
                    '<tr class="filaEduc">' +
                    '<th scope="row">1</th>' +
                    '<td><select name="educaciones-0-IdTipoEstu" class="form-control" id="id_educaciones-0-IdTipoEstu">' +

                    '<option value="1">Seleccione el tipo de educación</option>' +

                    '<option value="2">Pregrado</option>' +

                    '<option value="3">Tecnología</option>' +

                    '<option value="4">Técnica</option>' +

                    '<option value="5">Bachillerato</option>' +

                    '<option value="6">Postgrado</option>' +

                    '</select></td>' +
                    '<td><input type="text" name="educaciones-0-IdPaises" value class="form-control" id="id_educaciones-0-IdPaises"></td>' +
                    '<td><input type="text" name="educaciones-0-IdDepartamentos" value class="form-control" id="id_educaciones-0-IdDepartamentos"></td>' +
                    '<td><input type="text" name="educaciones-0-IdCiudades" value class="form-control" id="id_educaciones-0-IdCiudades"></td>' +
                    '<td><input type="text" name="educaciones-0-Instituto" value class="form-control" id="id_educaciones-0-Instituto"></td>' +
                    '<td><input type="text" name="educaciones-0-Titulo" value class="form-control" id="id_educaciones-0-Titulo"></td>' +
                    '<td><input type="text" name="educaciones-0-FechGrado" value class="form-control" id="id_educaciones-0-FechGrado"></td>' +
                    '<td><button data-num="1" class="btn btn-link iconTablas remove-form-row-educaciones" onclick="checkear(this,"educaciones")"><i class="fas fa-trash"></i></button></td>' +
                    '<td class="id-row"><input type="hidden" name="educaciones-0-id" value="" id="id_educaciones-0-id"></td>' +
                    '<td class="user-row"><input type="hidden" name="educaciones-0-IdUsuarios" value="' + idUser + '" class="form-control" id="id_educaciones-0-IdUsuarios"></td>' +
                    '</tr>'

                return nuevo;
            });
            break;
        case 'experiencias':
            $('#ExpContent').html(function () {
                var nuevo = '<input type="hidden" name="experiencias-TOTAL_FORMS" value="1" id="id_experiencias-TOTAL_FORMS"><input type="hidden" name="experiencias-INITIAL_FORMS" value="0" id="id_experiencias-INITIAL_FORMS"><input type="hidden" name="experiencias-MIN_NUM_FORMS" value="0" id="id_experiencias-MIN_NUM_FORMS"><input type="hidden" name="experiencias-MAX_NUM_FORMS" value="1000" id="id_experiencias-MAX_NUM_FORMS">' +


                    '<tr class="filaExp">' +
                    '<th scope="row">1</th>' +
                    '<td><select name="experiencias-0-IdCargos" class="form-control" id="id_experiencias-0-IdCargos">' +
                    '<option value="1">Seleccione el cargo</option>' +

                    '<option value="2">Profesor</option>' +

                    '<option value="3">Ingeniero</option>' +

                    '<option value="4">Administrador</option>' +

                    '</select>' +
                    '</td>' +
                    '<td><input type="text" name="experiencias-0-IdPaises" value="" class="form-control" id="id_experiencias-0-IdPaises"></td>' +
                    '<td><input type="text" name="experiencias-0-IdDepartamentos" value="" class="form-control" id="id_experiencias-0-IdDepartamentos"></td>' +
                    '<td><input type="text" name="experiencias-0-IdCiudades" value="" class="form-control" id="id_experiencias-0-IdCiudades"></td>' +
                    '<td><input type="text" name="experiencias-0-Empresa" value="" class="form-control" id="id_experiencias-0-Empresa"></td>' +
                    '<td><input type="text" name="experiencias-0-FechaIni" value="" class="form-control" id="id_experiencias-0-FechaIni"></td>' +
                    '<td><input type="text" name="experiencias-0-FechaFin" value="" class="form-control" id="id_experiencias-0-FechaFin"></td>' +
                    '<td><input type="text" name="experiencias-0-Funciones" value="" class="form-control" id="id_experiencias-0-Funciones"></td>' +
                    '<td><input type="text" name="experiencias-0-Logros" value="" class="form-control" id="id_experiencias-0-Logros"></td>' +
                    '<td><button data-num="1" class="btn btn-link iconTablas remove-form-row-experiencias" onclick="checkear(this,"experiencias")"><i class="fas fa-trash"></i></button></td>' +
                    '<td class="id-row"><input type="hidden" name="experiencias-0-id" value="" id="id_experiencias-0-id"></td>' +
                    '<td class="user-row"><input type="hidden" name="experiencias-0-IdUsuarios" value="' + idUser + '" class="form-control" id="id_experiencias-0-IdUsuarios"></td>' +


                    '</tr>'

                return nuevo;
            });
            break;
        case 'habilidades':
            $('#HabContent').html(function () {
                var nuevo = '<input type="hidden" name="habilidades-TOTAL_FORMS" value="1" id="id_habilidades-TOTAL_FORMS"><input type="hidden" name="habilidades-INITIAL_FORMS" value="0" id="id_habilidades-INITIAL_FORMS"><input type="hidden" name="habilidades-MIN_NUM_FORMS" value="0" id="id_habilidades-MIN_NUM_FORMS"><input type="hidden" name="habilidades-MAX_NUM_FORMS" value="1000" id="id_habilidades-MAX_NUM_FORMS">' +
                    '<tr class="filaHab">' +

                    '<th scope="row">1</th>' +
                    '<td><input type="text" name="habilidades-0-NombHabil" value="" class="form-control" id="id_habilidades-0-NombHabil"></td>' +
                    '<td><select name="habilidades-0-NiveHabil" class="form-control" id="id_habilidades-0-NiveHabil">' +
                    '<option value="Avanzado">Avanzado</option>' +

                    '<option value="Intermedio">Intermedio</option>' +

                    '<option value="Básico">Básico</option>' +

                    '</select></td>' +
                    '<td><button data-num="1" class="btn btn-link iconTablas remove-form-row-habilidades" onclick="checkear(this,"habilidades")"><i class="fas fa-trash"></i></button></td>' +

                    '<td class="id-row"><input type="hidden" name="habilidades-0-id" value="" id="id_habilidades-0-id"></td>' +
                    '<td class="user-row"><input type="hidden" name="habilidades-0-IdUsuarios" value="' + idUser + '" class="form-control" id="id_habilidades-0-IdUsuarios"></td>' +

                    '</tr>'

                return nuevo;
            });

            break;
        case 'logros':
            $('#LogContent').html(function () {
                var nuevo = '<input type="hidden" name="logros-TOTAL_FORMS" value="1" id="id_logros-TOTAL_FORMS"><input type="hidden" name="logros-INITIAL_FORMS" value="0" id="id_logros-INITIAL_FORMS"><input type="hidden" name="logros-MIN_NUM_FORMS" value="0" id="id_logros-MIN_NUM_FORMS"><input type="hidden" name="logros-MAX_NUM_FORMS" value="1000" id="id_logros-MAX_NUM_FORMS">' +

                    '<tr class="filaLog">' +
                    '<th scope="row">1</th>' +
                    '<td><select name="logros-0-idTipoLogr" class="form-control" id="id_logros-0-idTipoLogr">' +

                    '<option value="1">Seleccione el tipo de logro</option>' +

                    '<option value="2">Logro avanzado</option>' +

                    '<option value="3">Logro intermedio</option>' +

                    '<option value="4">Logro inferior</option>' +

                    '</select></td>' +
                    '<td><input type="text" name="logros-0-FechLogr" value="" class="form-control" id="id_logros-0-FechLogr"></td>' +
                    '<td><input type="text" name="logros-0-NombrLogr" value="" class="form-control" id="id_logros-0-NombrLogr"></td>' +
                    '<td><textarea name="logros-0-DescLogr" cols="150" rows="6" class="form-control" id="id_logros-0-DescLogr"></textarea></td>' +
                    '<td><button data-num="1" class="btn btn-link iconTablas remove-form-row-logros" onclick="checkear(this,"logros")"><i class="fas fa-trash"></i></button></td>' +
                    '<td class="id-row"><input type="hidden" name="logros-0-id" value="" id="id_logros-0-id"></td>' +
                    '<td class="user-row"><input type="hidden" name="logros-0-IdUsuarios" value="' + idUser + '" class="form-control" id="id_logros-0-IdUsuarios"></td>' +
                    '</tr>'

                return nuevo;
            });

            break;
    }
}

function añadirFila(selector, prefix) {
    var nuevoForm = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    var count = $('#' + prefix + 'Total').val();
    console.log(count);
    if (total == 0) {
        añadirPrimeraFila(prefix, total);
    } else {
        nuevoForm.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function () {
            var name = $(this).attr('name')
            if (name) {
                name = name.replace('-' + (total - 1) + '-', '-' + total + '-');
                var id = 'id_' + name;
                if (id == 'id_' + prefix + '-' + (total) + '-IdUsuarios') {
                    idUser = $('#id_datospersona-IdUsuarios').val()
                    $(this).attr({
                        'name': name,
                        'id': id
                    }).val(idUser).removeAttr('checked');
                } else {
                    $(this).attr({
                        'name': name,
                        'id': id
                    }).val('').removeAttr('checked');
                }
            }

        });
        nuevoForm.closest('tr').removeClass('deshabilitar');

        nuevoForm.find('th').html(function () {
            nuevo = parseInt(count) + 1;
            return nuevo;
        });
    }
    total++;
    count++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $('#' + prefix + 'Total').val(count);
    $(selector).after(nuevoForm);
    /*var conditionRow = $('.form-row:not(:last)');
    conditionRow.find('.btn.add-form-row')
    .removeClass('btn-success').addClass('btn-danger')
    .removeClass('add-form-row').addClass('remove-form-row')
    .html('<span class="glyphicon glyphicon-minus" aria-hidden="true"></span>');*/
    return false;

}

$(document).on('click', '.add-form-row-experiencias', function (e) {
    e.preventDefault();
    añadirFila('.filaExp:last', 'experiencias');
    return false;
});

$(document).on('click', '.remove-form-row-experiencias', function (e) {
    e.preventDefault();
    borrarFila('experiencias', '.filaExp', $(this));
    return false;
});

$(document).on('click', '.remove-form-row-experiencias', function (e) {
    e.preventDefault();
    checkear($(this), '.filaExp');
    return false;
});

$(document).on('click', '.add-form-row-habilidades', function (e) {
    e.preventDefault();
    añadirFila('.filaHab:last', 'habilidades');
    return false;
});

$(document).on('click', '.remove-form-row-habilidades', function (e) {
    e.preventDefault();
    borrarFila('habilidades', '.filaHab', $(this));
    return false;
});

$(document).on('click', '.remove-form-row-habilidades', function (e) {
    e.preventDefault();
    checkear($(this), '.filaHab');
    return false;
});

$(document).on('click', '.add-form-row-logros', function (e) {
    e.preventDefault();
    añadirFila('.filaLog:last', 'logros');
    return false;
});

$(document).on('click', '.remove-form-row-logros', function (e) {
    e.preventDefault();
    borrarFila('logros', '.filaLog', $(this));
    return false;
});

$(document).on('click', '.remove-form-row-logros', function (e) {
    e.preventDefault();
    checkear($(this), '.filaLog');
    return false;
});

$(document).on('click', '.add-form-row-educaciones', function (e) {
    e.preventDefault();
    añadirFila('.filaEduc:last', 'educaciones');
    return false;
});

$(document).on('click', '.remove-form-row-educaciones', function (e) {
    e.preventDefault();
    borrarFila('educaciones', '.filaEduc', $(this));
    return false;
});

$(document).on('click', '.remove-form-row-educaciones', function (e) {
    e.preventDefault();
    checkear($(this), '.filaEduc');
    return false;
});