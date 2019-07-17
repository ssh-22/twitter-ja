$(window).on('load', function(){
    $('img#profile.lazyload').lazyload();
});

$(window).on('load', function(){
    var csrftoken = Cookies.get('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});

$('button#follow-btn').on('submit', e=> {
    e.preventDefault();
    
    $.ajax({
        'url': '{% url "timeline:follow" %}',
        'type': 'POST',
        'data': {
            'username': $(this).prev().children('p').children('small').text()
        }
    })
})