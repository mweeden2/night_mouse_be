from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from nm import views


urlpatterns = [
    path('nm/', views.GameList.as_view()),
    path('nm/<int:pk>/', views.GameDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)