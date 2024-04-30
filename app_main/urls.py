from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('teachers/', views.teachers, name='teachers'),
    path('teacher/<int:id>/', views.teacher_detail, name='teacher_detail'),
    path('teacher/delete/<int:id>/', views.teacher_delete, name='teacher_delete'),
    path('teachers/new/', views.teacher_create, name='teacher_create'),
    path('teachers/update/<int:id>/', views.teacher_update, name='teacher_update'),

    path('students/new/<int:teacher_id>/', views.student_create, name='student_create'),
    path('student/<int:id>/', views.students_list, name='teacher_students'),
    path('student/delete/<uuid:student_id>/', views.student_delete, name='student_delete'),
    path('students/update/<uuid:student_id>/', views.student_update, name='student_update'),
    path('filtered-students/<int:hobby_id>/', views.filter_students, name='filter_students'), 
]
