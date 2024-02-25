
from django.urls import path
from .views import add_teacher_info

urlpatterns = [
    path('', add_teacher_info, name='add_teacher_info'),
]
