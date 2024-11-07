from django.shortcuts import render, redirect
from .forms import StudentInfoForm, StudentMarksForm
from .models import StudentInfo, StudentMarks

def student_info_view(request):
    if request.method == 'POST':
        form = StudentInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_info')
    else:
        form = StudentInfoForm()
    return render(request, 'student_app/student_info.html', {'form': form})

def student_marks_view(request):
    if request.method == 'POST':
        form = StudentMarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_marks')
    else:
        form = StudentMarksForm()
    return render(request, 'student_app/student_marks.html', {'form': form})