from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    #load the template
    template = loader.get_template('tag/index.html')

    #variables
    arr = ['Q1','Q2','Q3']

    #button
    answer = 'No response'
    if (request.POST.get('Q1_yes')):
        answer = 'YES'
    elif (request.POST.get('Q1_no')):
        answer = 'NO'

    hidd = request.POST.get('hidden')
    print 'reading input = ',hidd

    #create context to pass to the template
    context = {
        'arr':arr,
        'answer':answer,
    }
    return HttpResponse(template.render(context, request))
