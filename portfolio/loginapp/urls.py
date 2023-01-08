from django.urls import path
from . import views
app_name = 'loginapp'
urlpatterns = [
    path('register',views.Register,name='register'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
]

