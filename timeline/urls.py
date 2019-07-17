from django.urls import path
from timeline import views

app_name = 'timeline'
urlpatterns = [
    path('', views.TimelineList.as_view(), name='index'),
    path('tweet_add', views.tweet_add, name='tweet_add'),
    path('tweet_delete', views.tweet_delete, name='tweet_delete'),
    path('favorite_add', views.favorite_add, name='favorite_add'),
    path('favorite_delete', views.favorite_delete, name='favorite_delete'),
    path('search', views.SearchList.as_view(), name='search'),
]