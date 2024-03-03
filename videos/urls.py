from django.urls import path

from . import views as v

urlpatterns = [
    path('video/create', v.VideoCreateAPIView.as_view()),
    path('video/all', v.VideoListAPIView.as_view()),
    path('video/<int:pk>', v.VideoDetailAPIView.as_view()),
]
