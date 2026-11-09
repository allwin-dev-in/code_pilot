from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail

import os
from dotenv import load_dotenv

from django.contrib.auth.models import AbstractUser

load_dotenv()

# Create your models here.

class User(AbstractUser):
    phone=models.CharField(max_length=12,unique=True)

    ROLE_CHOICES=(
        ("student","student"),
        ("admin","admin")
    )
    role=models.CharField(max_length=100,choices=ROLE_CHOICES,default="student")

class StudentProfile(models.Model):

    skills = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    passoutyear = models.CharField(max_length=20,null=True)

    githuburl = models.URLField(null=True)

    linkedurl = models.URLField(null=True)

    student=models.OneToOneField(User,on_delete=models.CASCADE)


def create_student_profile(sender,instance,created,*args,**kwargs):
    if created and instance.role=="student":
        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,sender=User)

def send_invitation_mail(sender,instance,created,*args,**kwargs):
    if created and instance.role=="student":
        send_mail(
        "Account Creation Confirmation",
        f"""{instance.username}, Thank you for creating account in codepiolet application.
            you account details are \n 
            Username:{instance.username}\n
            Email:{instance.email}\n
            Phone:{instance.phone}\n""",
        {os.getenv("EMAIL_HOST_USER")},
        [instance.email],
        )

post_save.connect(send_invitation_mail,sender=User)
