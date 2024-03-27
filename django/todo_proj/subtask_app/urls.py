from django.urls import path
from .views import All_Subtasks, A_Subtask

urlpatterns = [
    path('', All_Subtasks.as_view(), name='all_subtasks'),
    path('<int:subtask_id>/', A_Subtask.as_view(), name='a_subtask'),
]
