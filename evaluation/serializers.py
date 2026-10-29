from rest_framework import serializers

from evaluation.models import Submission
from evaluation.models import Answer


from exams.models import Assessment
from exams.serializers import AssessmentSerializer

class SubmissionSerializer(serializers.ModelSerializer):

    assessment=serializers.StringRelatedField(read_only=True)
    student=serializers.StringRelatedField(read_only=True)

    answer_objects=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=Submission
        fields="__all__"
        read_only_fields=[fields]

    def get_answer_objects(self,obj):
        answer_objects=Answer.objects.filter(submission=obj)
        ser_inst=AnswerSerializer(answer_objects,many=True)
        return ser_inst.data





class AnswerSerializer(serializers.ModelSerializer):
    submission=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Answer
        fields="__all__"
        read_only_fields=["marks_awarded","feedback","evaluated_at","submission"]