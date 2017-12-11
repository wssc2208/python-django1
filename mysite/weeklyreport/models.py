from django.db import models

# Create your models here.
class weeklyUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.EmailField()

class WeeklyReportContent(models.Model):
    username = models.CharField(max_length=20)
    UpdateTime = models.DateTimeField('修改时间', auto_now=True)
    content = models.CharField(max_length = 100000)