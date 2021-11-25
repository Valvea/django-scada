from django.urls import path
from django.conf.urls import url
from .views import main_view,gant_view,save_tasks


app_name='main'

urlpatterns = [
    path('',main_view),
    path('gant/',gant_view,name='gant'),
    url(r'^get_json/', save_tasks, name='get_json'),

]
