from django.urls import path
from .views import (
    contacts_view, about_view, main_view
)

urlpatterns = [
    path('contacts/', contacts_view),
    path('about/', about_view),
    path('', main_view),
]
