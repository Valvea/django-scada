from django.shortcuts import render
import json
from django.http import HttpResponse,HttpResponseRedirect
import  os



def main_view(request):
    context={'name':'Саня'}
    return render(request, 'mainapp/main_page.html',context)


def gant_view(request):
    with open('./mainapp/static/mainapp/tasks.json',encoding='utf-8') as f:
        tasks=json.load(f)
        json_ob=json.dumps(tasks, ensure_ascii=False)
        dict_of_tasks={"tasks":tasks,"json_ob":json_ob}

    return render(request, 'mainapp/gant.html', dict_of_tasks )



def get_tasks(request):


    with open('./mainapp/static/mainapp/tasks.json',encoding='utf-8') as f:

        return HttpResponse(f, content_type='application/json; charset=utf-8',)



def add_task(request):

    task = dict(request.GET)

    with open('./mainapp/static/mainapp/tasks.json',encoding='utf-8',mode="r") as f:

        tasks=json.load(f)
        if tasks:
            dep=task['dependencies'][0].split(" ")
            dep=dep[1]+" "+dep[2]
            last_id=int(tasks[-1]['id'].split(' ')[1])+1
            print(last_id)

            task_to_json = {"start": task['start'][0],
                            "end": task['end'][0],
                            "name": task['name'][0],
                            "id": "Task " + str(last_id),
                            "progress": task['progress'][0],
                            "dependencies": dep,
                            "custom_class": 'bar-milestone'
                            }

        else:
            task_to_json = {"start": task['start'][0],
                            "end": task['end'][0],
                            "name": task['name'][0],
                            "id": "Task 0",
                            "progress": task['progress'][0],
                            "custom_class": 'bar-milestone'
                            }

    tasks.append(task_to_json)
    with open('./mainapp/static/mainapp/tasks.json', encoding='utf-8', mode="w") as f:
        json_ob = json.dumps(tasks, ensure_ascii=False)
        f.seek(0)
        f.write(json_ob)


    return HttpResponseRedirect('/gant')


def get_json_object(request):
    json_ob=dict(request.GET)
    print(json_ob)
    return HttpResponse(200)