from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .lsa import lsa_similarity
from .predict import predict_lab
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
        finger_sim = fingerprint_similarity(p1,p2)
        label = predict_lab(lsa_sim,finger_sim)
        sims = {
        "lsa_similarity" : lsa_sim,
        "fingerprint_similarity" : finger_sim,
        "plag_label" : label
        }
        return render(request, 'result.html', sims)
