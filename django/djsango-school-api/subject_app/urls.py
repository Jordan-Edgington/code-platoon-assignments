from django.urls import path, register_converter
from .views import All_Subjects, A_Subject

urlpatterns = [
    path('', All_Subjects.as_view(), name='all_subjects'),
    path('<str:subject>/', A_Subject.as_view(), name='a_subject')
]
