from django.urls import path
from nm import views


urlpatterns = [
    path('nm/', views.game_list),
    path('nm/<int:pk>/', views.game_detail)
]