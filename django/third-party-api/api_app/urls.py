from django.urls import path
from .views import Marvel

urlpatterns = [
    path('', Marvel.as_view(), name='marvel'),
]
