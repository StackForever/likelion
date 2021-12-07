from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'), # 10 자리에 post_id 라는 이름의 변수를 넣을 것이고, 이 변수의 type은 int형이다 라고 지정해줌.
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/like/', views.like, name='like'),
]