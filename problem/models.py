from django.db import models

from exams.models import Assessment
from accounts.models import User

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    score=models.PositiveIntegerField()
    assessment=models.ForeignKey(Assessment,on_delete=models.CASCADE)
    sample_input=models.TextField()
    sample_output=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
