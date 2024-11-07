from django import forms
from .models import StudentInfo, StudentMarks

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['name', 'mobile', 'hobbies']

class StudentMarksForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = ['student_name', 'subject', 'marks']
