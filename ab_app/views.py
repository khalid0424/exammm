from django.shortcuts import render
from rest_framework import viewsets
from .models import  Class , Class_notebook , Class_schedule ,Teacher ,Student
from .serializers import ClassSerializer , Class_notebookSerializer , Class_scheduleSerializer , TeacherSerializer, StudentSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class Class_notebookViewSet(viewsets.ModelViewSet):
    queryset = Class_notebook.objects.all()
    serializer_class = Class_notebookSerializer

class Class_scheduleViewSet(viewsets.ModelViewSet):
    queryset = Class_schedule.objects.all()
    serializer_class = Class_scheduleSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer







