from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .lsa import lsa_similarity
from .word_sim import word_similarity
from .finger_sim import fingerprint_similarity

def home(request):
    context = {
        "variable1" : "mishan thapa",
        "result" : "kshetri"
    }
    return render(request, 'home.html',context)

def check(request):

    lsa_sim = None
    word_sim = None
    if request.method == "POST":
        p1 = (request.POST["paragraph1"])
        p2 = (request.POST["paragraph2"])
        lsa_sim = lsa_similarity(p1,p2)
        #word_sim = word_similarity(p1,p1)
        finger_sim = fingerprint_similarity(p1,p2)
        sims = {
        "lsa_similarity" : lsa_sim,
        #"word_similarity" : word_sim,
        "fingerprint_similarity" : finger_sim
        }
        return render(request, 'result.html', sims)
