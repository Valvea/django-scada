from django.urls import path
from .views import main_view,gant_view

urlpatterns = [
    path('',main_view),
    path('gant/',gant_view)
]