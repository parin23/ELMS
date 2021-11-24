from django.db import models

class stModel(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=100)
    class Meta:
        db_table = "student"