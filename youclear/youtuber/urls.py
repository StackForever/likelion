from django.urls import path
from .views import *

app_name='youtuber'

urlpatterns = [
    path('', index, name="index"),    
    path('youtuber/<int:youtuber_id>/', youtuber, name="youtuber"),
    path('add/my_youtuber/<int:youtuber_id>/', add_my_youtuber, name='add_my_youtuber'), 
    path('remove/my_youtuber/<int:youtuber_id>/', remove_my_youtuber, name='remove_my_youtuber'),
    path('my_youtuber/<int:user_id>/', my_youtuber, name='my_youtuber'),
    path('edit_my_youtuber/<int:user_id>/', edit_my_youtuber, name="edit_my_youtuber"),
    path('delete_my_youruber/<int:youtuber_id>/', delete_my_youtuber, name="delete_my_youtuber"),
    path('my_list/<int:user_id>/', my_list, name="my_list"),
]