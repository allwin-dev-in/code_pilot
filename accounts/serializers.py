from rest_framework import serializers

from accounts.models import User
from accounts.models import StudentProfile



class UserSerializer(serializers.ModelSerializer):

    details=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=User
        fields=["id","username","email","password","phone","role","details"]
    def get_details(self,obj):
        qs=StudentProfile.objects.filter(student_id=obj)
        ser_inst=StudentProfileSerializer(qs,many=True)
        return ser_inst.data

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentProfile
        fields="__all__"
        read_only_fields=["id","student"]