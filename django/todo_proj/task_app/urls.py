from django.urls import path, include
from .views import All_Tasks, A_Task

urlpatterns = [
    path('', All_Tasks.as_view(), name='all_tasks'),
    path('<int:task_id>/', A_Task.as_view(), name='a_task'),
    path('<int:task_id>/subtasks/', include('subtask_app.urls'))
]
