from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.shortcuts import render
from django.http import HttpResponse


def main_view(request):
    # template = Template(
    #     'Hello {{ name }}'
    # )
    # context = Context({
    #     'name': 'Anton'
    # })
    # response_string = template.render(context)

    # template = get_template('main/index.html')

    # context = {
    #     'title': 'This is a main page',
    #     'subtitle': 'First django page',
    #     'username': request.user,
    # }

    # response_string = template.render(context)

    response_string = render_to_string(
        'main/index.html',
        {
            'title': 'This is a main page',
            'subtitle': 'First django page',
            'username': request.user,
            'is_active': False
        }
    )

    # return render(request, 'main/index.html')
    return HttpResponse(response_string)


def contacts_view(request):
    return render(
        request, 
        'main/contacts.html',
        {
            'contacts': [
                '8900007500',
                '8900007501',
                '8900007502',
            ]
        }
    )


def about_view(request):
    return render(
        request, 
        'main/about.html',
        {
            'text': 'Несмотря на сложности, гидродинамический удар гасит эллиптический погранслой.'
        }
    )
