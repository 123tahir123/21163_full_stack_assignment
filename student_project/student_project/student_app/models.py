from django.db import models

class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    hobbies = models.TextField()

    def __str__(self):
        return self.name

class StudentMarks(models.Model):
    student_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.subject}"
    

