from random import shuffle

#importing the local preprocessing function
from .preprocessing import punc_removal
from .preprocessing import tokenization

def fingerprint_similarity(p1,p2):
    p1 = punc_removal(p1)
    p2 = punc_removal(p2)
    t1 = tokenization(p1)
    t2 = tokenization(p2)
    str1=""
    str2=""
    for ele in t1:
        str1 = str1 + ele +" "
    
    for ele in t2:
        str2 = str2 + ele +" "
    def shingle(text:str,k:int):
        shingle_set =[]
        for i in range(len(text)-k+1):
            shingle_set.append(text[i:i+k])
        return set(shingle_set)

    d1 = shingle(str1,2)
    d2 = shingle(str2,2)

    vocab = list(d1.union(d2))

    d1_en =[1 if x in d1 else 0 for x in vocab]
    d2_en =[1 if x in d2 else 0 for x in vocab]


    def create_hash(size:int):
        hash_ex = list(range(1,len(vocab)+1))
        shuffle(hash_ex)
        return hash_ex

    def build_minhash_func(vocab_size:int,nbits:int):
        hashes=[]
        for _ in range(nbits):
            hashes.append(create_hash(vocab_size))
        return hashes
    #creates a array of 64bit hash
    minhash_func =build_minhash_func(len(vocab),64)

    def create_hash(vector: list):
        # use this function for creating our signatures (eg the matching)
        signature = []
        for func in minhash_func:
            for i in range(1, len(vocab)+1):
                idx = func.index(i)
                signature_val = vector[idx]
                if signature_val == 1:
                    signature.append(idx)
                    break
        return signature

    a_sig = create_hash(d1_en)
    b_sig = create_hash(d2_en)

    def jaccard(x,y):
        return len(x.intersection(y))/len(x.union(y))

    val = jaccard(set(a_sig),set(b_sig))
    return val