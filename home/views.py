from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json
from difflib import get_close_matches

def index(request):
    return render(request, "index.html")

def mean(request):
    data=json.load(open('static/dictionary.json'))
    if request.method == 'POST':
        word=request.POST.get('word')
        
        
        if word in data:
            context={'data':data[word]}
            return render(request,'mean.html',context)


        elif len(get_close_matches(word,data.keys()))>1:
            context={'data':get_close_matches(word,data.keys())}
            # print(context)
            # preference = {}
            # newList = []
            # newList.append(context['data'][0])
            # preference['data'] = newList
            # print("===========================")
            # print(preference)
            # print("===========================")
            ctx = {'data': data[context['data'][0]]}
            return render(request,'mean.html',ctx)

    return HttpResponse('sorry')