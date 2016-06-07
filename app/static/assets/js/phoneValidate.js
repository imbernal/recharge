/**
 * Created by imbernal on 6/1/16.
 */
$(document).ready(function() {
    $('#form')
        .find('[name="_phone"]')
            .intlTelInput({
                utilsScript: 'static/assets/js/utils.js',
                autoPlaceholder: true,
                preferredCountries: ['fr', 'us', 'gb']
            });

});