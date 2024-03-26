from django.urls import path
from grade_app.views import A_Grade, All_Grades
urlpatterns = [
    path('', All_Grades.as_view(), name='all_grades'),
    path('<int:id>/', A_Grade.as_view(), name='a_grade')
]
