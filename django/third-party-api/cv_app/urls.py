from django.urls import path
from .views import Comic_Vine

urlpatterns = [
    path('', Comic_Vine.as_view(), name='comic_vine')
]
