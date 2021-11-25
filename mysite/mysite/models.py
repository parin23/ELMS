from django.db import models

class stModel(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=100)
    class Meta:
        db_table = "student"

class teachModel(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=100)
    class Meta:
        db_table = "teacher"

class cnameModel(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=100)
    class Meta:
        db_table = "course_type"

class resultModel(models.Model):
    result_no = models.IntegerField(primary_key=True)
    course_id = models.IntegerField()
    test_id = models.IntegerField()
    student_id = models.IntegerField()
    score = models.IntegerField()
    result_date = models.DateField()
    cal_cpi = models.IntegerField(null=True)
    class Meta:
        db_table = "result"