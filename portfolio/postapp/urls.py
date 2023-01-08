from django.urls import path
from . import views
app_name = 'postapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('create_post', views.create_post, name='create_post'),
    path('edit_post', views.edit_post, name='edit_post'),
    path('delete_post/<pk>', views.delete_post, name='delete_post'),
    path('post_details/<pk>', views.post_details, name='post_details'),
    path('follow_view/<username>', views.follow_view, name='follow_view'),
    path('unfollow_view/<username>', views.unfollow_view, name='unfollow_view'),
    # path('myposts', views.myposts, name='myposts'),
]
