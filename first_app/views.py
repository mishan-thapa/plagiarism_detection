from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#importing the local preprocessing function
from .lsa import lsa_similarity
from .predict import predict_lab
from .finger_sim import fingerprint_similarity
from .word_sim import calculate_wordsimilarity
from .ngrams_sim import ngrams_similarity

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
        str1 = (request.POST["paragraph1"])
        str2 = (request.POST["paragraph2"])
        

        
        lsa_sim = lsa_similarity(str1,str2)
        finger_sim = fingerprint_similarity(str1,str2)
        word_sim = calculate_wordsimilarity(str1,str2)
        ngram_sim = ngrams_similarity(str1,str2,2)
        label = predict_lab(lsa_sim,finger_sim,word_sim,ngram_sim)
        sims = {
        "lsa_similarity" : lsa_sim,
        "fingerprint_similarity" : finger_sim,
        "word_sim" : word_sim,
        "ngram_sim" : ngram_sim,
        "plag_label" : label
        }
        return render(request, 'result.html', sims)



def tryy(request):
    return render(request, 'try.html')