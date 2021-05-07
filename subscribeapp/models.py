from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')
    class Meta:
        # 유저와 프로젝트 각각의 한 쌍이 오직 하나만 존재하게 된다.
        unique_together = ('user', 'project')
