from django.urls import path, register_converter
from .views import All_Students, A_Student, Add_Subject_To_Student

urlpatterns = [
    path('', All_Students.as_view(), name='all_students'),
    path('<int:id>/', A_Student.as_view(), name='a_student'),
    path('<int:id>/subject/<int:subject_id>/',
         Add_Subject_To_Student.as_view(), name='add_subject_to_student')
]
