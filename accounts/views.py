from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


from accounts.serializers import UserSerializer
from accounts.serializers import StudentProfileSerializer
from accounts.models import User
from accounts.models import StudentProfile

from evaluation.permissions import IsStudentUser

# Create your views here.

class AdminCreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            qs=User.objects.create_superuser(**cleaned_data,role="admin")
            serializer_instance=UserSerializer(qs)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class StudentCreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            qs=User.objects.create_user(**cleaned_data)
            serializer_instance=UserSerializer(qs)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class ProfileUpdateView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated,IsStudentUser]

    def put(self,request):
        form_data=request.data
        user_profile_Object=get_object_or_404(StudentProfile,student=request.user)
        serializer_instance=StudentProfileSerializer(data=form_data,instance=user_profile_Object)

        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            StudentProfile.objects.filter(student_id=request.user).update(**cleaned_data)
            return Response(serializer_instance.validated_data)
        else:
            return Response(serializer_instance.errors)

class ProfileDetailView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated,IsStudentUser]

    def get(self,request):
        qs=User.objects.get(username=request.user)
        ser_inst=UserSerializer(qs)
        return Response(data=ser_inst.data)