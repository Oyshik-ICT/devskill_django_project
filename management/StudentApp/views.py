from django.shortcuts import render, redirect
from .Forms import StudentForm


def add_student_info(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_student_info')
    else:
        form = StudentForm()
        return render(request, 'student_page.html', {'form': form})