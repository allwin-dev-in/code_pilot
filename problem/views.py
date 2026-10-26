from django.shortcuts import render

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication
from rest_framework import permissions

from problem.serializers import QuestionSerializer
from problem.models import Question
# Create your views here.

class QuestionListView(ListAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=QuestionSerializer
    queryset=Question.objects.all()

class QuestionCreateView(CreateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    serializer_class=QuestionSerializer

class QuestionRetriveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=QuestionSerializer
    queryset=Question.objects.all()