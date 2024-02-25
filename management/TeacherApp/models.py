from django.db import models

class Info(models.Model):
    teacher_id = models.IntegerField()
    teacher_name = models.CharField(max_length = 20)
    teacher_subject = models.CharField(max_length = 10)
    teacher_address = models.CharField(max_length = 10)

