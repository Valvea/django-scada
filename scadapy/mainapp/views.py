from django.shortcuts import redirect, render
from django.core import serializers
import json
from django.http import HttpResponse,HttpResponseRedirect
import  os
from .models import Task

def main_view(request):
    context={'name':'Сепя'}
    return render(request, 'mainapp/main_page.html',context)


def gant_view(request):
    
    tasks=Task.objects.all()
    json_ob=serializers.serialize('json',tasks)
    return render(request,'mainapp/gant.html',{"json_ob":json_ob})





def manage_task(request):
    
    dict_of_task= json.loads(request.POST.get('data_'))
   
    match dict_of_task['task']:
        

        case 'add':
            print('case add')
            print(dict_of_task['tasks']['id'])
            Task.objects.create(id=dict_of_task['tasks']['id'],
                                name=dict_of_task['tasks']['name'],
                                start=dict_of_task['tasks']['start'],
                                end=dict_of_task['tasks']['end'],
                                progress=dict_of_task['tasks']['progress'],
                                dependencies=dict_of_task['tasks']['dependencies'],
                                custom_class=dict_of_task['tasks']['custom_class'])
            

        case 'del':
            task_id=int( dict_of_task['tasks'].split('Task')[1])
            print(task_id)
            task=Task.objects.get(id=task_id)
            task.delete()
            

    return HttpResponseRedirect('/gant')


    



