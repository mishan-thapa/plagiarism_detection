from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#importing the local preprocessing function
from .nepali_tfidf import calculate_tfidfsimilarity
from .predict import predict_lab
#from .finger_sim import fingerprint_similarity
#from .word_sim import calculate_wordsimilarity
from .ngrams_sim import overlap_similarity

def home(request):
    context = {
        "variable1" : "mishan thapa",
        "result" : "kshetri"
    }
    return render(request, 'home.html',context)

def check(request):
    #lsa_sim = None
    if request.method == "POST":
        str1 = (request.POST["paragraph1"])
        str2 = (request.POST["paragraph2"])
        lsa_sim = calculate_tfidfsimilarity(str1,str2)
        #finger_sim = fingerprint_similarity(str1,str2)
        ngram_sim = overlap_similarity(str1,str2,3)
        label = predict_lab(lsa_sim,ngram_sim)
        sims = {
        "tfidf_similarity" : lsa_sim,
        "ngram_sim" : ngram_sim,
        "plag_label" : label
        }
        return render(request, 'result.html', sims)



def tryy(request):
    return render(request, 'try.html')

from .models import tfiles

def upload(request):
    if request.method == 'POST':
        print("run vayo hai")
        print(request.FILES)
        f1 = request.FILES.get("fileone")
        #print(f1)
        f2 = request.FILES.get("filetwo")
        #print(f2)
        f1_text = f1.read()
        f2_text = f2.read()
        #print(f1_text)
        #print(type(f1_text))
        f11_text = f1_text.decode()
        f22_text = f2_text.decode()
        #print(type(f11_text))
        print(f11_text)
        ngram_sim = overlap_similarity(f11_text,f22_text,2)
        lsa_sim = calculate_tfidfsimilarity(f11_text,f22_text)
        #finger_sim = fingerprint_similarity(f11_text,f22_text)
        #word_sim = calculate_wordsimilarity(f11_text,f22_text)
        label = predict_lab(lsa_sim,ngram_sim)
        sims = {
        "lsa_similarity" : lsa_sim,
        "ngram_sim" : ngram_sim,
        "plag_label" : label
        }
        #return HttpResponse("success")
        return render(request, 'result.html', sims)
        
