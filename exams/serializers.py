from rest_framework import serializers

from exams.models import Assessment

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assessment
        fields="__all__"
        read_only_fields=["id","end_time","created_by","created_at","updated_at"]