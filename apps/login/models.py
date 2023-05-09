from django.db import models
import datetime

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username
    
class Tasks(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    started_at = models.DateField(auto_now=True)
    finish_by = models.DateField(default=datetime.date(2023,1,1))

    def __str__(self) -> str:
        return self.user.username + " Task No." + str(self.pk)
