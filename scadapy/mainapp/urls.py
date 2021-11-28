from django.urls import path
from django.conf.urls import url
from .views import main_view,gant_view,manage_task


app_name='main'

urlpatterns = [
    path('',main_view),
    path('gant/',gant_view,name='gant'),
    url(r'/mangetask/', manage_task, name='mangetask'),

]
