from django.db import models



class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    sername = models.CharField(max_ength=100)
    class_name = models.CharField(max_length=10)

    phone_number= models.CharField(max_length=2)

    def __str__(self):
        return self.name
    
class Class_notebook(models.Model):

    id = models.IntegerField(primary_key=True)
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    absent = models.BooleanField(default=False)
    unabsent = models.BooleanField(default=False)
    late = models.BooleanField(default=False)
    homework = models.BooleanField(default=False)
    homework_comment = models.TextField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    count_day_absent = models.IntegerField(default=0)
    count_day_unabsent = models.IntegerField(default=0)
    count_day_late = models.IntegerField(default=0)
    time = models.TimeField(blank=True, null=True)
    date = models.DateField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    sername = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Class_schedule(models.Model):
    id = models.IntegerField(primary_key=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=10)
    time = models.TimeField()

    def __str__(self):
        return self.subject