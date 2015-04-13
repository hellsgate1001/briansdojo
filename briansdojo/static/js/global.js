$(window).load(function(){
    if ($('#contact_success').length > 0) {
        $('#contact-link').click();
    }

    if ($('form .error').length > 0) {
        $('#contact-link').click();
    }

    $('form').submit(function(event){
        if ($('form input, form textarea').length > 0) {
            passed = true;
            failed = false;
            $('form input, form textarea').each(function(index, element){
                if (!check_element($(this))) {
                    passed = false;
                    failed = $(this);
                    return false;
                }
            });

            if (passed !== true) {
                show_required(failed);
                $('#contact-link').click();
                event.preventDefault();
            }
        }
    });
});

function show_required(element) {
    if ($(element).attr('placeholder').indexOf('This field is required.') < 0) {
        $(element).attr('placeholder')+= ': This field is required.';
    }
    $(element).focus();
}

function check_element(element) {
    if (
        ($(element).is('input') && $(element).val() == '') ||
        ($(element).is('textarea') && $(element).text() == '')
    ) {
        return false;
    }

    return true;
}
