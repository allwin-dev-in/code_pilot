from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView
from rest_framework import serializers

from exams.models import Assessment

from problem.models import Question

from evaluation.models import Submission
from evaluation.models import Answer
from evaluation.permissions import IsStudentUser
from evaluation.serializers import SubmissionSerializer
from evaluation.serializers import AnswerSerializer

# Create your views here.

class SubmissionStartView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsStudentUser]

    def post(self,request,pk=None):
        assessment_id=pk
        assessemnt_object=get_object_or_404(Assessment,id=assessment_id)

        instance=Submission.objects.create(assessment=assessemnt_object,student=request.user)
        
        serializer_instance=SubmissionSerializer(instance)
        return Response(data=serializer_instance.data)

class SubmissionRetriveView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request,pk=None):
        instance=get_object_or_404(Submission,id=pk)
        serializer_instance=SubmissionSerializer(instance)

        return Response(serializer_instance.data)


class AnswerCreate(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsStudentUser]
    def post(self,request,pk=None):
        submission_id=pk
        submission_object=get_object_or_404(Submission,id=submission_id)
        form_data=request.data

        #validation
        assessment_object=submission_object.assessment
        assessment_questions=Question.objects.filter(assessment=assessment_object).values_list("id",flat=True) #for geting id's dict as flat in list
        question_id=form_data.get("question")

        if question_id not in assessment_questions:
            raise serializers.ValidationError("Question does not exist in assessment")

        serializer_instanace=AnswerSerializer(data=form_data)
        if serializer_instanace.is_valid():
            serializer_instanace.save(submission=submission_object,question_id=question_id)
            return Response(serializer_instanace.data)
        else:
            return Response(serializer_instanace.errors)

class AnswerRetriveView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]
    def get(self,request,pk=None):
        instance=get_object_or_404(Answer,id=pk)

        serializer_instance=AnswerSerializer(instance)
        return Response (serializer_instance.data)

class AnswerEvaluateView(UpdateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=AnswerSerializer
    queryset=Answer.objects.all()



    def patch(self,request,pk=None):
        answer_id=pk
        answer_object=get_object_or_404(Answer,id=answer_id)
        form_data=request.data
        serializer_instance=AnswerSerializer(data=form_data,instance=answer_object,partial=True)
        serializer_instance.fields["marks_awarded"].read_only=False
        serializer_instance.fields["feedback"].read_only=False

        #Validation (marks)
        question_object=Question.objects.filter(title=answer_object.question)
        question_mark=question_object["score"]
        print(question_mark)

        if serializer_instance.is_valid():
            # Answer.objects.filter(id=answer_id).update(**form_data)
            serializer_instance.save()

            return Response(serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

