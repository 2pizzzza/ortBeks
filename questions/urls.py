from django.urls import path
from . import views as v

urlpatterns = [
    path('create', v.QuestionCreateAPIView.as_view()),
    path('all', v.QuestionListAPIView.as_view()),
    path('<int:pk>', v.QuestionDetailAPIView.as_view()),
    path('<int:pk>/answer/all', v.AnswerListAPIView.as_view()),

    path('answer/create', v.AnswerCreateAPIView.as_view()),
    path('answer/<int:pk>', v.AnswerDetailAPIView.as_view()),
]
