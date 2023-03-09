import pandas as pd
import nltk
import numpy as np
from nltk import ngrams

from .n_preprocess import word_tokenize
from .n_preprocess import word_stemmer
from .n_preprocess import stopword_removal
from .n_preprocess import remove_english_from_nepali

def preprocess(text):
    tokens = word_tokenize(text)
    stemmed_tokens = word_stemmer(tokens)
    removed_tokens=stopword_removal(stemmed_tokens)
    return removed_tokens


def n_grams(text,n):
    tokens=list(preprocess(text))
    grams = list(ngrams(tokens, n))
    return grams 

def overlap_similarity(text1, text2,n):
    grams1=n_grams(text1,n)
    grams2=n_grams(text2,n)
    # Convert the bigrams lists to sets
    set1 = set(grams1)
    set2 = set(grams2)
    A = set(set1)
    B = set(set2)
    numerator = len(A.intersection(B))
    min_len = min(len(A), len(B))
    if min_len==0:
        jaccard_similarity=0
    else:
        jaccard_similarity = numerator/min_len
    return round(jaccard_similarity,2)