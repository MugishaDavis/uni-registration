from registration.models.department import Department
from django.db import models
from django.db.models.deletion import CASCADE


class Application(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(to=Department,on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    status = models.CharField(max_length=70, default="PENDING")
    date = models.DateField(auto_now_add=True)
