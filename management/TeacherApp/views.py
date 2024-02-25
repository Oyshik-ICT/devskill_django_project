from django.shortcuts import render, redirect
from .Forms import TeacherForm

def add_teacher_info(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_teacher_info')
    else:
        form = TeacherForm()
        return render(request, 'teacher_page.html', {'form' : form})