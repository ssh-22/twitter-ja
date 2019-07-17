$(window).on('load', function(){
    $('img#profile.lazyload').lazyload();
});

$(function(){
    $('button#unfollow-btn').hover(function(){
        $('button#unfollow-btn').text("フォロー解除");
        $('button#unfollow-btn').removeClass('is-info');
        $('button#unfollow-btn').addClass('is-danger');
    }, function(){
        $('button#unfollow-btn').text("フォロー中");
        $('button#unfollow-btn').removeClass('is-danger');
        $('button#unfollow-btn').addClass('is-info');
    });
});

