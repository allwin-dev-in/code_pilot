from django.db import models

from datetime import datetime,time,timedelta

from accounts.models import User

# Create your models here.

class Assessment(models.Model):
    title=models.CharField(max_length=100)
    batch=models.CharField(max_length=200)
    LANGUAGE_CHOICES=(
        ("python","python"),
        ("java","java"),
        ("php","php")
    )
    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES)
    exam_date=models.DateField()
    start_time=models.TimeField()
    duration=models.PositiveIntegerField()
    end_time=models.TimeField(null=True)
    STATUS_CHOICES=(
        ("active","active"),
        ("inactive","inactive")
    )
    status=models.CharField(max_length=100,choices=STATUS_CHOICES)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args,**kwargs):
        end_date_time = datetime.combine(self.exam_date, self.start_time) + timedelta(hours=self.duration)
        self.end_time = end_date_time.time()

        return super().save(*args,**kwargs)
   