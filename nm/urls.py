from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from nm import views


urlpatterns = [
    path('', views.api_root),
    path('games/', 
        views.GameList.as_view(),
        name='game-list'),
    path('games/<int:pk>/',
        views.GameDetail.as_view(),
        name='game-detail'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)