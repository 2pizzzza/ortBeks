from django.urls import path

from . import views as v
from questions import views as qv
from .views import TestUserByUserAPIView

urlpatterns = [
    path('create', v.TestCreateAPIView.as_view()),
    path('all', v.TestListAPIView.as_view()),
    path('<int:pk>', v.TestDetailAPIView.as_view()),
    path('<int:pk>/question/all', qv.QuestionListAPIView.as_view()),

    path('submit', v.TestUserCreateAPIView.as_view()),
    path('all/result', v.TestUserListAPIView.as_view()),
    path('<int:pk>/result', v.TestUserDetailAPIView.as_view()),
    path('getallbyuser/', TestUserByUserAPIView.as_view(), name='get_all_by_user'),
]
