import pandas as pd
import nltk
import numpy as np
from nltk import ngrams


from .preprocessing import punc_removal
from .preprocessing import stopword_removal
from .preprocessing import tokenization

def ngrams_similarity(p1,p2,n):
    p1 = punc_removal(p1)
    p2 = punc_removal(p2)
    t1 = tokenization(p1)
    t2 = tokenization(p2)
    s1 = stopword_removal(t1)
    s2 = stopword_removal(t2)
    str1=""
    str2=""
    for ele in s1:
        str1 = str1 + ele +" "
    
    for ele in s2:
        str2 = str2 + ele +" "
    bigrams1 = [" ".join(bigram) for bigram in ngrams(str1, n)]
    bigrams2 = [" ".join(bigram) for bigram in ngrams(str2, n)]
    set1 = set(bigrams1)
    set2 = set(bigrams2)
    A = set(set1)
    B = set(set2)
    numerator = len(A.intersection(B))
    min_len = min(len(A), len(B))
    jaccard_similarity = numerator/min_len
    return jaccard_similarity