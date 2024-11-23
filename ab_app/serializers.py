from rest_framework import serializers

from .models import Student , Class_notebook ,Class_schedule, Class , Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class Class_notebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_notebook
        fields = '__all__'

class Class_scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_schedule
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'





