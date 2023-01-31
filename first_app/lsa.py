#importing the library for TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
#import the libraries for SVD
from sklearn.decomposition import TruncatedSVD
import numpy as np
#import library for cosine similarity
import pandas as pd


from .preprocessing import punc_removal
from .preprocessing import stopword_removal
from .preprocessing import tokenization


def lsa_similarity(p1,p2):
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
    docs = [str1,str2]
    vectorizer = TfidfVectorizer()
    dictionary = vectorizer.fit_transform(docs)
    inarr = dictionary.todense().tolist()

    # Create a TruncatedSVD object with 2 components
    svd = TruncatedSVD(n_components=2)

    # Fit the object to the matrix X
    svd.fit(inarr)

    U = svd.components_
    
    UT = U.T
    
    Sigma = svd.singular_values_
    
    V = svd.transform(inarr)

    array1 = V[0]
    array2 = V[1]

    ## calculation for the similarity
    numerator=np.dot(array1,array2)

    denom=np.sqrt(sum(np.square(array1)))*np.sqrt(sum(np.square(array2)))

    # Similarity:
    result = round(numerator/denom,3)
    return result
