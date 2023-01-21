from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .lsa import lsa_similarity

def home(request):
    context = {
        "variable1" : "mishan thapa",
        "result" : "kshetri"
    }
    return render(request, 'home.html',context)

def check(request):
    result = None
    if request.method == "POST":
        p1 = (request.POST["paragraph1"])
        p2 = (request.POST["paragraph2"])
        result = lsa_similarity(p1,p2)


    return render(request, 'result.html', {'result' : result})
