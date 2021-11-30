from django.shortcuts import redirect, render
from django.core import serializers
from django.http import HttpResponse,HttpResponseRedirect
from django.db import transaction
import json
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
            
        case 'change':
            print(dict_of_task['tasks'])
            fields=['start','end','progress']
            tasks_ids=set(list(dict_of_task['tasks']['data_change'].keys())+list(dict_of_task['tasks']['progress_changed'].keys()))
            print(tasks_ids)
            tasks=list(map(lambda x:Task.objects.get(id=x),tasks_ids))
            print(tasks)
            for task in tasks:
                    if str(task.id) in dict_of_task['tasks']['data_change']:
                        print('ya tut')
                        task.start=dict_of_task['tasks']['data_change'][str(task.id)]['start']
                        task.end=dict_of_task['tasks']['data_change'][str(task.id)]['end']
                    if str(task.id) in dict_of_task['tasks']['progress_changed']:
                        print('ya tut')
                        task.progress=dict_of_task['tasks']['progress_changed'][str(task.id)]['progress']

            Task.objects.bulk_update(tasks,fields)
                    



                        



               


            # for task_id in dict_of_task['tasks']['data_change']:
            #         task=Task.objects.get(id=task_id)
            #         task.start=dict_of_task['tasks']['data_change'][task_id]['start']
            #         task.end=dict_of_task['tasks']['data_change'][task_id]['end']
            #         tasks.append(task)
            # for task_id in dict_of_task['tasks']['progress_changed']:
            #         task=Task.objects.get(id=task_id)
            #         task.progress=dict_of_task['tasks']['progress_changed'][task_id]['progress']
            #         tasks.append(task)    
                

                # tasks_ids=list(dict_of_task['tasks']['data_change'].keys())+list(dict_of_task['tasks']['progress_changed'].keys())
                # tasks=list(map(lambda x:Task.objects.get(id=x),tasks_ids)
                # for task in tasks:
                #     setattr(task,)
                    
                


                # with transaction.atomic():
                #     for data_change,progress_changed in  zip(dict_of_task['tasks']['data_change'],dict_of_task['tasks']['progress_changed']):
                #                 for task in data_change:
                #                     taskdb=Task.objects.get(id=task)
                #                     taskdb.start=data_change[task]['start']
                #                     taskdb.end=data_change[task]['end']
                #                 for task in progress_changed:
                #                     taskdb=Task.objects.get(id=task)
                #                     taskdb.progress=progress_changed[task]['progress']
                #     taskdb.save()
                                
                                
                                
                            
                        

                    # for task_ in dict_of_task['tasks']:
                    #     for key,task in task_.items():
                    #         taskdb=Task.objects.get(id=task['id'])
                    #         match key:
                    #             case 'data_change':
                    #                 taskdb.start=task['start']
                    #                 taskdb.end=task['end']
                                
                    #             case 'progress_changed':
                    #                 taskdb.progress=task['progress']
                                    
                    
                
            
                 
                   




    return HttpResponseRedirect('/gant')


    



