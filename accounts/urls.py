from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('<username>/', views.AccountDetailView.as_view(), name='detail'),
    path('<username>/follow', views.follow, name='follow'),
    path('<username>/unfollow', views.unfollow, name='unfollow'),
    path('<username>/edit', views.edit, name='edit'),
]