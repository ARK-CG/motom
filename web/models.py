from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#User=>https://docs.djangoproject.com/en/2.0/ref/contrib/auth/

# Create your models here.
"""例
class Card(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    liked = models.IntegerField(default=0)
    card_date = models.DateTimeField('date published', default=timezone.now)
    card_tag = models.TextField()
    card_caregory = models.TextField()
    user = models.ForeignKey(User,related_name='cards',on_delete=models.CASCADE,default="0")
"""

class Project(models.Model):
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    context = models.TextField()
    support = models.IntegerField(default=0)
    max_member = models.IntegerField(default=0)
    make_date = models.DateTimeField('date published', default=timezone.now)
    start_date = models.DateTimeField('date published', default=timezone.now)
    end_date = models.DateTimeField('date published', default=timezone.now)

class Task(models.Model):
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    context = models.TextField()

class Table_auth(models.Model):
    project_id = models.ForeignKey(Project, related_name='projects', on_delete=models.CASCADE, default="0")
    user_id = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE, default="0")

class Table_task(models.Model):
    project_id = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE, default="0")
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, default="0")

class Table_tag(models.Model):
    status = models.BooleanField(default=True)
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE, default="0")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default="0")
    task =  models.ForeignKey(Task, on_delete=models.CASCADE, default="0")