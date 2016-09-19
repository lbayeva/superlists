jQuery(document).ready(function ($) {
   $(document).on("keypress click", ":input", function ( event ) {
        $('.has-error').hide();
   });
});
