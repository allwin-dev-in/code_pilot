from django.urls import path

from exams.views import AssesmentListView
from exams.views import AssesmentCreateView
from exams.views import AssessmentRetriveUpdateDeleteView

urlpatterns=[
    path("all/",AssesmentListView.as_view()),
    path("add/",AssesmentCreateView.as_view()),
    path("<int:pk>/",AssessmentRetriveUpdateDeleteView.as_view()),

]