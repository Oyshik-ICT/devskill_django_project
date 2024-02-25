from django import forms
from .models import Info

class StudentForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['student_id', 'student_name', 'student_class', 'student_address']