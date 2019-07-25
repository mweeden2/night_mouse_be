from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from nm import views


urlpatterns = [
    path('nm/', views.game_list),
    path('nm/<int:pk>/', views.game_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)