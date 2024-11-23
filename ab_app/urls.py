from views import * 
from django.urls import path , include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentapi',StudentViewSet,basename='student')
router.register('teacherapi',TeacherViewSet,basename='teacher')
router.register('classapi',ClassViewSet,basename='class')
router.register('subjectapi',Class_notebookViewSet,basename='subject')
router.register('schudeleapi',Class_scheduleViewSet,basename='schudele')

urlpatterns = [
    
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]


