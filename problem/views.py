from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response

from exams.models import Assessment

from problem.serializers import QuestionSerializer
from problem.models import Question

# Create your views here.

class QuestionListView(ListAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=QuestionSerializer
    queryset=Question.objects.all()

# class QuestionCreateView(CreateAPIView):
#     authentication_classes=[authentication.TokenAuthentication]
#     permission_classes=[permissions.IsAdminUser]

#     serializer_class=QuestionSerializer
#     def perform_create(self, serializer):
#         assessment_id=self.kwargs.get("pk")
#         assessment_object=Assessment.objects.get(id=assessment_id)
#         serializer.save(assessment=assessment_object,created_by=self.request.user)
class QuestionCreateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def post(self,request,pk=None):
        assessment_object=Assessment.objects.get(id=pk)
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(assessment=assessment_object,created_by=request.user)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)



class QuestionRetriveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=QuestionSerializer
    queryset=Question.objects.all()