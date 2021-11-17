from django.shortcuts import render


def main_view(request):
    context={'name':'Саня'}
    return render(request, 'mainapp/main_page.html',context)


def gant_view(request):
    return render(request, 'mainapp/gant.html',)