from django.urls import path

from evaluation.views import SubmissionStartView
from evaluation.views import SubmissionRetriveView
from evaluation.views import AnswerCreate
from evaluation.views import AnswerRetriveView
from evaluation.views import AnswerEvaluateView

urlpatterns=[
    path("assessment/<int:pk>/submission/start/",SubmissionStartView.as_view()),
    path("submission/<int:pk>/",SubmissionRetriveView.as_view()),
    path("submission/<int:pk>/answer/",AnswerCreate.as_view()),
    path("answer/<int:pk>/",AnswerRetriveView.as_view()),
    path("answer/evaluate/<int:pk>/",AnswerEvaluateView.as_view()),
   
    
]