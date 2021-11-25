from django.shortcuts import render
import json
from django.http import HttpResponse,HttpResponseRedirect
import  os



def main_view(request):
    context={'name':'Сепя'}
    return render(request, 'mainapp/main_page.html',context)


def gant_view(request):
    with open('./mainapp/static/mainapp/tasks.json',encoding='utf-8') as f:
        tasks=json.load(f)
        json_ob=json.dumps(tasks, ensure_ascii=False)
        dict_of_tasks={"tasks":tasks,"json_ob":json_ob}

    return render(request, 'mainapp/gant.html', dict_of_tasks )




def save_tasks(request):

    with open('./mainapp/static/mainapp/tasks.json', encoding='utf-8', mode="w") as f:
        json_str = str(request.GET).split("<QueryDict: ")[1][2:-9]
        f.seek(0)
        f.write(json_str)

    return HttpResponse(200)