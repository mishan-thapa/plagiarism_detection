import pandas as pd
import csv
import nltk
import numpy as np
import re
from random import shuffle
from nltk.tokenize import word_tokenize




import string
import nltk
class tokenize:
    def __init__(self):
        pass
    def word_tokenize(self,text):
        self.text = text
        import string
        punctuations = list(string.punctuation)
        # Add the Nepali purnabiram to the list of punctuations
        punctuations.append("।")
        punctuations.append("”")
        punctuations.append("“")
        punctuations.append("’")
        punctuations.append("‘")
        for punctuation in punctuations:
            self.text = self.text.replace(punctuation, ' ')
        self.text = self.text.strip().split()
        return self.text
    
    def __str__(self):
        return "return the tokenized text removing the punctuations"
    



import snowballstemmer

class stemming:
    def __init__(self):
        self.stemmer = snowballstemmer.NepaliStemmer()

    def word_stemmer(self, tokens):
        if isinstance(tokens, str):
            tokens = tokens.split()
        stemmed_tokens = [self.stemmer.stemWord(token) for token in tokens]
        return stemmed_tokens

    def __str__(self):
        return "stemming is done on Nepali words and returns the list of stemmed words."





stopwords_list = ['', 'सं', 'यहाँसम्', 'यहाँसम्म', 'आफैँ', 'उनले', 'त्यसम', 'जसल', 'गयौ', 'धन्न', 'निकै', 'पर्थ्य', 'राख्छ', 'आफू',
                  'तिमीसँ', 'ए', 'नत्', 'अन्तर्ग', 'दर्ता', 'त', 'लागि', 'आफ्नै', 'गर्', 'क्रमश', 'भयेन', 'तापन', 'यत', 'तिनीहरूल',
                  'भन्', 'यथोचि', 'आज', 'फरक', 'ल', 'उ', 'आएका', 'द्वारा', 'यस्तो', 'रही', 'सोचेको', 'रुपमा', 'उनि', 'कारण',
                  'चाहनुहुन्छ', 'दोस्रो', 'तत्का', 'हुनेछ', 'दिएको', 'तेह्र', 'अन्यत्', 'या', 'मला', 'सबै', 'तथ', 'राम्रो', 'सबैको', 'भा',
                  'उक्त', 'आदि', 'पहिल', 'पछिल्ल', 'हुन्थ', 'र', 'दे', 'गर्नुपर्', 'दिनुहुन्', 'त्य', 'दोस्र', 'दि', 'चोटी', 'दिए',
                  'अन्तर्गत', 'कसैको', 'तापनि', 'हाम्रा', 'गर्यौ', 'पर्ने', 'आफ', 'तेस्र', 'सँग', 'हुन', 'जस्तै', 'बन', 'तपाईको', 'ती',
                  'हुँदै', 'थिएन', 'भनेको', 'उनल', 'जसलाई', 'तिनीहरूको', 'हुन्', 'प्रत', 'धौ', 'कोहिपनि', 'औं', 'कोहीपनि', 'घर',
                  'पहिल्यै', 'संग', 'यद्यप', 'मध्ये', 'यसक', 'गरेको', 'सम', 'जहा', 'पहिल्य', 'भयो', 'जसबाट', 'थिए', 'जो', 'अरू',
                  'रे', 'कहिलेकाहीं', 'सा', 'सारा', 'ले', 'तिनिहरुलाई', 'पांच', 'त्यस्तो', 'जसम', 'प्लस', 'भने', 'भन्न', 'तपा',
                  'जनाको', 'अरुलाई', 'भएक', 'सहितै', 'गर्द', 'भन्द', 'किन', 'छन्', 'तुरुन्तै', 'साथै', 'बाट', 'त्यसले', 'सङ्ग',
                  'आफूला', 'तथापि', 'त्यसैले', 'विशे', 'तीन', 'उसलाई', 'जुन', 'निर्दिष्ट', 'तिर', 'लाख', 'कोहि', 'यस्त', 'यसपछ',
                  'माथी', 'आजको', 'यस', 'उन्नाइस', 'चाहेको', 'पछाडी', 'बिशे', 'भएर', 'राम्र', 'के', 'पिच्छे', 'कुनै', 'अठार',
                  'बार', 'अरु', 'उन', 'जता', 'थि', 'राखे', 'दुब', 'धेर', 'त्यसपछ', 'आदिलाई', 'भए', 'तेस्रो', 'आए', 'गर्छ',
                  'भएन', 'जसक', 'प्रते', 'सबैलाई', 'यस्तै', 'अझै', 'थरि', 'उनको', 'हर', 'सोध्', 'ग', 'यसले', 'अलग', 'सत्र',
                  'भित्र', 'फेरि', 'गै', 'पर्छ', 'निम्ति', 'आफनो', 'देखेको', 'सहित', 'मेरो', 'सरह', 'भरि', 'माथ', 'राख', 'अनुसा',
                  'आफ्नो', 'एकदम', 'ठाउँमा', 'न', 'तिनै', 'सँगसँगै', 'कहिल्य', 'व', 'सक्', 'तिनी', 'अर्था', 'नि', 'हामीसँ', 'तैपनी',
                  'नगर्नु', 'नभनेर', 'छैनन्', 'सम्भ', 'नयाँ', 'आएको', 'यहाँ', 'तिनीहरूला', 'रहेछ', 'सँगको', 'बताए', 'थियो', 'लाग', 
                  'तता', 'त्सपछ', 'पन्ध्र', 'रह', 'जोपनि', 'सकदि', 'छु', 'चाहि', 'जस्तोसुक', 'जबकी', 'सङ्गको', 'भनेर', 'देखि',
                  'ऊ', 'सही', 'चाहिए', 'बिच', 'उनलाई', 'त्यहाँ', 'कता', 'सँ', 'ह', 'एउटा', 'आफैल', 'गरी', 'साथ', 'देखेक',
                  'गरेक', 'बीचम', 'मुन्तिर', 'कस्त', 'भन्छन', 'लाई', 'गएको', 'हुनु', 'एउट', 'यथोचित', 'मध्य', 'उस्त', 'पक्कै', 
                  'भन्ने', 'यो', 'समयम', 'आफूलाई', 'उदाहरण', 'नजिक', 'का', 'यद', 'तिरको', 'यसबाहेक', 'उहा', 'कसैसँग', 'कि',
                  'गरौं', 'बाह्र', 'प्रतेक', 'विरुद्', 'वटा', 'हुन्थ्यो', 'हाम्र', 'थिएनन', 'कतै', 'कुन', 'पक्क', 'नजिकै', 'त्यहीँ', 'सब',
                  'लागेको', 'कस', 'भन्नुभय', 'यद्ध्यपि', 'बने', 'कृपया', 'शायद', 'धेरै', 'उनी', 'कुन्नी', 'नत्रभने', 'हुने', 'थरी', 'मात्रै',
                  'चाहीं', 'साय', 'अघि', 'ला', 'केह', 'अ', 'थिय', 'यसको', 'सोह्र', 'तेश्रो', 'पो', 'सक्दै', 'चाहन्छु', 'सक्ने', 'जे',
                  'निम्', 'अवस्था', 'कसरी', 'तेस्कारण', 'दिनुभएको', 'भएँ', 'तिनीहरुक', 'कहा', 'आजक', 'उप', 'बीच', 'थ', 'देखिन्छ',
                  'जसरी', 'अन्यत्र', 'बन्', 'बी', 'भएकालाई', 'गरेर', 'जुनै', 'चाल', 'पाचौँ', 'तर्फ', 'अरुला', 'अझ', 'म', 'कसै',
                  'जनाले', 'गैर', 'सम्भव', 'हरे', 'सुरु', 'त्यत्तिकैमा', 'बिचमा', 'देखिय', 'तैपनि', 'सोचेर', 'सुनेर', 'तेस्कार', 'तिनीहरू',
                  'नै', 'यसो', 'बाहिर', 'पाँचौ', 'पर्याप्त', 'निम्न', 'जना', 'हाम्रो', 'त्यो', 'कहिल', 'मलाई', 'उनीहरुको', 'मुख्य', 'हामी',
                  'देखेर', 'उनीहर', 'यहा', 'वरीपरी', 'त्सपछि', 'कसैल', 'जस्तोसुकै', 'मा', 'जाहिर', 'मुनि', 'पाँचौं', 'अर्क', 'तिनि',
                  'चाँड', 'आफैला', 'तर', 'पर्नेमा', 'संगै', 'पनि', 'कसैले', 'देखिन्', 'देखे', 'देख्', 'त्यसको', 'भन्नुभयो', 'भएका',
                  'काम', 'कसैलाई', 'स्पष्', 'भन्दा', 'प्ल', 'अक्स', 'नत्र', 'त्सैल', 'फेरी', 'झैं', 'तब', 'पछी', 'रू', 'स',
                  'कहिलेकाही', 'अगाडि', 'गर्ने', 'सम्म', 'जबक', 'जसबा', 'पहिले', 'भन', 'तदनुसार', 'नभएको', 'तपाई', 'जनालाई',
                  'समय', 'थप', 'केही', 'भन्छन्', 'तपाईक', 'अलि', 'यसका', 'छू', 'क', 'अनुसार', 'आद', 'अहिले', 'बरु', 'तसरी',
                  'को', 'कुरा', 'रहेका', 'त्यस्तै', 'ज', 'तिम्र', 'गरे', 'छैन', 'फेर', 'यसमा', 'वा', 'गरेका', 'बिरुद्', 'आय', 'गर्छु',
                  'त्यहिँ', 'अर्थात', 'हैन', 'चाहेर', 'हामीले', 'हुँदैन', 'दु', 'अनि', 'अन्यथ', 'पर्दैन', 'बिशेष', 'पर्थ्यो', 'हुनुहुन्', 'जा',
                  'छन', 'उहाला', 'जाने', 'देख', 'त्यस', 'हुनत', 'अब', 'तथा', 'सधै', 'हुन्छ', 'वरीपर', 'एकद', 'सोह', 'ओठ', 
                  'कम से क', 'किनभने', 'चौथो', 'रहेको', 'हजार', 'होल', 'नगर्नुहोस', 'बिरुद्ध', 'दोश्री', 'स्थित', 'आफै', 'रूप',
                  'अन्य', 'जसले', 'लगायत', 'जोपनी', 'तथापी', 'गर्दै', 'साँच्च', 'जस्ता', 'वास्तवम', 'त्यसकार', 'यसबाहे', 'वाहे',
                  'पछिल्लो', 'अन्यथा', 'देखियो', 'जु', 'निर्दिष्', 'अर्थात्', 'कति', 'भन्छु', 'सुरुमै', 'अक्सर', 'तिनीहरूक', 'तल',
                  'लगभग', 'होइ', 'सो', 'सकिए', 'पछि', 'यति', 'मैल', 'तुरन्त', 'जसको', 'जस्त', 'त्यहा', 'तिमी', 'गरौ', 'भित्',
                  'प्रत्ये', 'लगभ', 'दोश्र', 'गर्न', 'आफ्न', 'औ', 'कमसेकम', 'वास्तवमा', 'मुख्', 'पछाडि', 'अरूला', 'गए', 'राख्', 'ठूलो',
                  'त्यसो', 'गर्नेछ', 'गर्नेछन', 'यसपछि', 'स्पष्ट', 'जस्तो', 'होइनन', 'त्यही', 'दिनुभएक', 'थिएँ', 'थाहा', 'पक्का', 'भ',
                  'य', 'कही', 'हु', 'अर', 'चौध', 'त्यहीं', 'आत्', 'होला', 'हाम', 'पर्याप्', 'जसला', 'भीत्र', 'उसला', 'सध', 'बाहे',
                  'बढी', 'भन्या', 'बा', 'यही', 'चाहिंले', 'वापत', 'होस', 'भरी', 'गर्नु', 'केव', 'सट्टा', 'जतातत', 'निम्त', 'होइन',
                  'सार', 'गर्नुपर्छ', 'सुरुको', 'द्वार', 'वाट', 'दुइ', 'गर', 'अर्को', 'त्यसकारण', 'कस्तो', 'त्यत्तिकै', 'बिस', 'पट', 'गएर',
                  'छै', 'हरेक', 'एउटै', 'भन्छ', 'पर्', 'अगाडी', 'अगाड', 'दुइवटा', 'कहाँबाट', 'कसर', 'चाहनुहुन्', 'निम्नानुसा', 'सुनेको',
                  'यसैल', 'पन', 'यदि', 'ठी', 'भर', 'अल', 'पछ', 'बारेम', 'आयो', 'गर्दा', 'जबकि', 'वरिपर', 'चाले', 'ठीक',
                  'तुरुन्त', 'मेर', 'कोही', 'चाहन्छौ', 'कहाँबा', 'जाहि', 'तिनीहरु', 'यसरी', 'निम्नानुसार', 'चाहन्छ', 'त्सैले', 'उसले', 'कम',
                  'जसमा', 'जहाँ', 'नगर्नू', 'जान', 'तपाइँक', 'एघार', 'माथि', 'गरि', 'मात्र', 'कोह', 'उसको', 'प्रति', 'बाहेक', 'सँगै',
                  'हो', 'दोश्रो', 'चाहिं', 'बारे', 'त्यसैल', 'यसर', 'उनक', 'दिन', 'किनभन', 'चा', 'बर', 'तापनी', 'जताततै', 'उहालाई',
                  'सक्छ', 'नभई', 'भित्री', 'अधि', 'अन्', 'तिनिहरुला', 'कसरि', 'कत', 'जब', 'शाय', 'तदनुसा', 'पाँ', 'यद्यपि', 'सट्ट',
                  'बीस', 'यी', 'सोही', 'मात्', 'चाहन्थ', 'बीचमा', 'मार्फ', 'सह', 'छौ', 'साँच्चै', 'तत्काल', 'नया', 'सबैला', 'ति',
                  'आ', 'तपाइ', 'सायद', 'पहिलो', 'प्राय', 'ओ', 'सम्', 'दिनुहुन्छ', 'पटक', 'हामीला', 'छौं', 'बाहि', 'गय', 'समेत',
                  'होकि', 'उहाँला', 'प्रत्यक', 'अथवा', 'भन्दै', 'मैले', 'कुर', 'क्रमशः', 'तिम', 'कृपय', 'तिनीहर', 'पूर्व', 'उदाहर',
                  'भएको', 'रहेक', 'सय', 'केहि', 'गर्छन्', 'आत्म', 'पूर्', 'तिनीहरुको']





class stopwords:
    def __init__(self):
        pass
    
    def stopword_removal(self,tokens):
        self.tokens = tokens
        new_tokens = list() #new_tokens hold the list of words after removing stopwords
        for token in self.tokens:
            if token not in stopwords_list:
                new_tokens.append(token)
        return new_tokens

    def __str__(self):
        return "returns the tokens after removing stopwords"
    




def remove_english_from_nepali(nepali_text):
    # Define regular expression to match English words and characters
    english_pattern = re.compile(r'[a-zA-Z]+')
    
    # Remove English words and characters from the Nepali text
    nepali_text = re.sub(english_pattern, '', nepali_text)
    
    # Return the cleaned Nepali text
    return nepali_text





def preprocess(text):
    tokenizer = tokenize()
    stemmer=stemming()
    stop_removal=stopwords()
    tokens = tokenizer.word_tokenize(text)
    stemmed_tokens = stemmer.word_stemmer(tokens)
    removed_tokens=stop_removal.stopword_removal(stemmed_tokens)
    return removed_tokens




import hashlib

def winnowing(text, k, w):
    """
    Winnowing algorithm for text fingerprinting using MD5 as a non-cryptographic hash.

    Parameters:
        text (str): The input text to be fingerprinted.
        k (int): Length of the shingles (substring length).
        w (int): Size of the winnowing window.

    Returns:
        set: Set of winnowed hash values forming the fingerprint.
    """
    def hash_shingle(shingle):
        md5_hash = hashlib.md5(shingle.encode('utf-8'))
        return md5_hash.hexdigest()

    def generate_shingles(text, k):
        return {text[i:i+k] for i in range(len(text) - k + 1)}

    def winnow(shingles, w):
        min_hash_positions = []
        for i in range(len(shingles) - w + 1):
            window = list(shingles)[i:i+w]
            min_hash = min((hash_shingle(shingle) for shingle in window))
            min_hash_positions.append(min_hash)
        return set(min_hash_positions)

    shingles = generate_shingles(text, k)
    winnowed_hashes = winnow(shingles, w)
    return winnowed_hashes

def overlap_similarity(set1, set2):
    numerator = len(set1.intersection(set2))
    min_len = min(len(set1), len(set2))
    if min_len==0:
        overlap_similarity=0
    else:
        overlap_similarity = numerator/min_len
    return overlap_similarity





def fingerprint_similarity(text1,text2) :
    shingle_length = 5
    winnowing_window =5
    f1= winnowing(" ".join(preprocess(text1)),shingle_length,winnowing_window)
    f2= winnowing(" ".join(preprocess(text2)),shingle_length,winnowing_window)
    fingerprint_sim = overlap_similarity(f1,f2)
    result = round(fingerprint_sim,3)
    return result