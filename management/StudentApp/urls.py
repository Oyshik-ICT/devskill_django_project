from django.urls import path, include
from .views import add_student_info

urlpatterns = [
    path('add_student', add_student_info, name = 'add_student_info' ),
]
