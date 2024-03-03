from django.urls import path
from . import views

urlpatterns = [
    path('create', views.NewsCreateAPIView.as_view()),
    path('all', views.NewsListAPIView.as_view()),
    path('<int:pk>', views.NewsDetailAPIView.as_view()),
]
