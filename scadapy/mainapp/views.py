from django.shortcuts import render
import json
from django.http import HttpResponse
import  os


def main_view(request):
    context={'name':'Саня'}
    return render(request, 'mainapp/main_page.html',context)


def gant_view(request):
    return render(request, 'mainapp/gant.html', )



def task_view(request):

    task=dict(request.GET)
    obj={}
    for k,v in task.items():
       obj.update({k:v[0]})

    json_object = json.dumps(obj, indent=4)


    return render(request, 'mainapp/gant.html',obj)

def get_tasks(request):

    with open('test.json') as f:

        return HttpResponse(f,content_type='application/json')