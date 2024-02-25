from django import forms
from .models import Info

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['teacher_id', 'teacher_name', 'teacher_subject', 'teacher_address']