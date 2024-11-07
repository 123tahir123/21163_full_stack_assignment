from django.urls import path
from . import views

urlpatterns = [
    path('student_info/', views.student_info_view, name='student_info'),
    path('student_marks/', views.student_marks_view, name='student_marks'),
]
