from django.urls import path
from django.conf.urls import url
from .views import main_view,gant_view,get_tasks,add_task,save_tasks

urlpatterns = [
    path('',main_view),
    path('gant/',gant_view),
    url(r'^tasks.json/', get_tasks, name='tasks.json'),
    url(r'^addtask/', add_task, name='addtask'),
    url(r'^get_json/', save_tasks, name='get_json'),

]
