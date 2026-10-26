from django.urls import path

from problem.views import QuestionListView
from problem.views import QuestionCreateView
from problem.views import QuestionRetriveUpdateDeleteView


urlpatterns=[
    path("question/all/",QuestionListView.as_view()),
    path("assessment/<int:pk>/question/",QuestionCreateView.as_view()),
    path("question/<int:pk>/",QuestionRetriveUpdateDeleteView.as_view()),

]