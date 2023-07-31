from django.urls import path
from .views import student_list, add_student, update_student, delete_student

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/add/', add_student, name='add_student'),
    path('students/<int:pk>/update/', update_student, name='update_student'),
    path('students/<int:pk>/delete/', delete_student, name='delete_student'),
]
