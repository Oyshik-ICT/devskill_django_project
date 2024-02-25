from django.db import models

class Info(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length = 20)
    student_class = models.IntegerField()
    student_address = models.CharField(max_length = 20)
