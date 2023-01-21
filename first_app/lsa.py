#importing the library for TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
#import the libraries for SVD
from sklearn.decomposition import TruncatedSVD
import numpy as np
#import library for cosine similarity
import pandas as pd

def lsa_similarity(p1,p2):
    docs = [p1,p2]
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
