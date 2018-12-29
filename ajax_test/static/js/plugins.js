$(document).ready(function() {
  var tiny_form = $("#tiny-form");

  tiny_form.on('submit', function(e) {
    e.preventDefault();
    // Get form data and serialize it.
    var form_data = $(this).serialize();

    // Get form destination url.
    var form_url = $(this).attr('data-url') || window.location.href;
    console.log(form_url);

    // Make form ajax post request.
    $.ajax({
      url: form_url,
      type: 'POST',
      data: form_data
    })
    .done(function(data) {
      console.log(data.msg);
    })
    .fail(function(data) {
      console.log(data.msg);
    })

  })
});
