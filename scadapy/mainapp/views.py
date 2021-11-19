from django.shortcuts import render
from django.http import HttpResponse

def main_view(request):
    context={'name':'Саня'}
    return render(request, 'mainapp/main_page.html',context)


def gant_view(request):
    return render(request, 'mainapp/gant.html', )



def task_view(request):
    # Get the variable text
    print(request.GET)
    # Do whatever with the input variable text

    # Send the response

    return HttpResponse(request)

