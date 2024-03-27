from django.urls import path, include
from .views import All_Lists, A_List

urlpatterns = [
    path('', All_Lists.as_view(), name='all_lists'),
    path('<int:list_id>/', A_List.as_view(), name='a_list'),
    path('<int:list_id>/tasks/', include('task_app.urls'))
]
