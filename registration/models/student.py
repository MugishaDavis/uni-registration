from registration.models.application import Application
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    application = models.ForeignKey(to=Application, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)

