from django.urls import path
from django.conf.urls import url
from .views import main_view,gant_view,task_view,get_tasks

urlpatterns = [
    path('',main_view),
    path('gant/',gant_view),
    url(r'^addtask/',task_view,name='addtask'),
    url(r'data.json/',get_tasks,name='obj')

]
