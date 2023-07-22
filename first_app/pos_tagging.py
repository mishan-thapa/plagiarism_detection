import tensorflow
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import warnings
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model


suffixes = {'अगाडि','अगावै','अगि','अघि','अतिरिक्त','अनुकूल','अनुरुप','अनुरूप','अनुसार','अन्तरगत',
            'अन्तर्गत','अन्तर्गत्','अर्न्तगत','अलावा','उपर','उप्रान्त','कन','कहाँ','का','काँ','की',
            'कै','को','कों','खातिर','खेरि','गरिसकी','छेउ','जत्ति','जत्रा','जत्रै','जसमध्ये','जसै',
            'जसो','जस्ता','जस्ती','जस्तै','जस्तो','झै','झैँ','झैं','तक','तक्','तर्फ','तल','ताक',
            'ताका','तिर','तिरै','तिर्','तीर','थर','थरी','देखि','देखिन','देखिनै','देखिन्','देखी','द्वारा',
            'धरी','नगिचै','नजिक','नजिकै','निकट','निमित','निमित्त','निम्ति','निम्नबमोजिम','निम्नानुसार',
            'निर','निहित','नीर','नुसार','नेर','पछाडि','पछाडिपट्टि','पछि','पछी','पट्टि','पट्टी','पनि',
            'पर','परक','पर्यन्त','पश्चात','पश्चात्','पश्चिमपट्टि','पारि','पारिपट्टि','पारी','पिच्छे',
            'पूर्व','पूर्वक','प्रति','प्रभृति','बमोजिम','बाट','बाटै','बापत','बारे','बाहिर','बाहेक',
            'बिच','बित्तिकै','बिना','बीच','बेगर','भन्दा','भन्ने','भर','भरि','भरी','भित्र','भित्रै',
            'मध्ये','मनि','मन्','मा','माझ','माथि','मारे','मार्फत','मार्फत्','मुताविक','मुनि',
            'मूलक','मै','मैं','यता','रूपी','लगायत','लगि','लाइ','लाई','लाईं','लागि','लागी','ले',
            'ले.','वरिपरि','वस','वाट','वाट्','वापत','वारि','वारे','वाला','विच','वित्तिकै','विना',
            'विरुद्ध','विरूद्ध','सँग','सँगसँगै','सँगै','संग','संगै','सङ्ग','समक्ष','समेत','सम्बन्धि',
            'सम्बन्धी','सम्म','सम्मत','सम्मन','सम्मै','सम्वन्धी','सरह','सरि','सरी','सहित','साथ',
            'साथसाथै','साथै','सामु','सामुन्ने','सित','सिवाय','सीत','स्थित','स्वरूप','हर','हरु','हरू','हाले'}


# Create a dictionary to map specific NELRALEC tags to their generalized POS tags
pos_mapping = {
    # Noun
    'NN': 'Noun',
    'NP': 'Noun',
    
    # Pronoun
    'PMX': 'Pronoun',
    'PTN': 'Pronoun',
    'PTM': 'Pronoun',
    'PTH': 'Pronoun',
    'PXH': 'Pronoun',
    'PXR': 'Pronoun',
    'PMXKM': 'Pronoun',
    'PMXKF': 'Pronoun',
    'PMXKO': 'Pronoun',
    'PTNKM': 'Pronoun',
    'PTNKF': 'Pronoun',
    'PTNKO': 'Pronoun',
    'PTMKM': 'Pronoun',
    'PTMKF': 'Pronoun',
    'PTMKO': 'Pronoun',
    'PRFKM': 'Pronoun',
    'PRFKF': 'Pronoun',
    'PRFKO': 'Pronoun',
    'PMXKX': 'Pronoun',
    'PTNKX': 'Pronoun',
    'PTMKX': 'Pronoun',
    'PRFKX': 'Pronoun',
    'PRF': 'Pronoun',

    # Determiner
    'DDM': 'Determiner',
    'DDF': 'Determiner',
    'DKM': 'Determiner',
    'DKF': 'Determiner',
    'DJM': 'Determiner',
    'DJF': 'Determiner',
    'DGM': 'Determiner',
    'DGF': 'Determiner',
    'DDO': 'Determiner',
    'DKO': 'Determiner',
    'DJO': 'Determiner',
    'DGO': 'Determiner',
    'DDX': 'Determiner',
    'DKX': 'Determiner',
    'DJX': 'Determiner',
    'DGX': 'Determiner',
    'RD': 'Determiner',
    'RK': 'Determiner',
    'RJ': 'Determiner',
    
    # Verb
    'VVMX1': 'Verb',
    'VVMX2': 'Verb',
    'VVTN1': 'Verb',
    'VVTX2': 'Verb',
    'VVYN1': 'Verb',
    'VVYX2': 'Verb',
    'VVTN1F': 'Verb',
    'VVTM1F': 'Verb',
    'VVYN1F': 'Verb',
    'VVYM1F': 'Verb',
    'VOMX1': 'Verb',
    'VOMX2': 'Verb',
    'VOTN1': 'Verb',
    'VOTX2': 'Verb',
    'VOYN1': 'Verb',
    'aVOYX2': 'Verb',
    'VI': 'Verb',
    'VN': 'Verb',
    'VDM': 'Verb',
    'VDF': 'Verb',
    'VDO': 'Verb',
    'VDX': 'Verb',
    'VE': 'Verb',
    'VQ': 'Verb',
    'VCN': 'Verb',
    'VCM': 'Verb',
    'VCH': 'Verb',
    'VS': 'Verb',
    'VR': 'Verb',

    # Adjective
    'JM': 'Adjective',
    'JF': 'Adjective',
    'JO': 'Adjective',
    'JX': 'Adjective',
    'JT': 'Adjective',

    # Adverb
    'RR': 'Adverb',

    # Postposition
    'II': 'Postposition',
    'IH': 'Postposition',
    'IE': 'Postposition',
    'IA': 'Postposition',
    'IKM': 'Postposition',
    'IKO': 'Postposition',
    'IKF': 'Postposition',
    'IKX': 'Postposition',
    
    # Numerals
    'MM': 'Numerals',
    'MOM': 'Numerals',
    'MOF': 'Numerals',
    'MOO': 'Numerals',
    'MOX': 'Numerals',
    
    # Classifier
    'MLM': 'Classifier',
    'MLF': 'Classifier',
    'MLO': 'Classifier',
    'MLX': 'Classifier',
    
    # Conjunction
    'CC': 'Conjunction',
    'CSA': 'Conjunction',
    'CSB': 'Conjunction',
    
    # Interjection
    'UU': 'Interjection',
    
    # Question Marker
    'QQ': 'Question Marker',
    
    # Particle
    'TT': 'Particle',
    
    # Punctuation
    'YF': 'Punctuation',
    'YM': 'Punctuation',
    'YQ': 'Punctuation',
    'YB': 'Punctuation',
    
    # Foreign Word
    'FF': 'Foreign Word',
    'FS': 'Foreign Word',
    'FO': 'Foreign Word',
    'FZ': 'Foreign Word',
    
    # Unclassifiable
    'FU': 'Unclassifiable',
    
    # Abbreviation
    'FB': 'Abbreviation',
    
    # NULL Tag
    'NULL': 'NULL Tag',
}

def sentence_tokenize(text):
    sentences = text.strip().split('।')
    sentences = [sentence.strip() + ' ।' for sentence in sentences if sentence.strip()]
    return sentences

def word_tokenize(sentences):
    tok_sentences = []
    punctuations = [',', ';', '?', '!', '—', '-', '.','’','‘']
    for sentence in sentences:
        for punctuation in punctuations:
            sentence = sentence.replace(punctuation, ' ')

        sentence = sentence.strip().split()
        tok_sentences.append(sentence)
    return tok_sentences

def stem_word(word):
    stem = word
    suffixes_found = []

    while True:
        found_suffix = False
        for suffix in suffixes:
            if stem.endswith(suffix):
                stem = stem[:len(stem) - len(suffix)]
                suffixes_found.append(suffix)
                found_suffix = True
                break

        if not found_suffix:
            break

    return stem, suffixes_found[::-1]

def stem_words(tok_sentences):
    stemmed_sentences = []
    for sentence in tok_sentences:
        stemmed_words = []

        for word in sentence:
            stemmed_word, suffixes_found = stem_word(word)
            if stemmed_word or suffix:
                if stemmed_word:
                    stemmed_words.append(stemmed_word)
                if suffixes_found:
                    stemmed_words.extend(suffixes_found)
        
        stemmed_sentences.append(stemmed_words)
    return stemmed_sentences

def pos_tagging_function(sentence):
    random.seed(0)
    warnings.filterwarnings("ignore")
    data = pd.read_csv('first_app/book_pos.csv', encoding = 'utf-8')
    data = data.fillna(method="ffill") # Deal with N/A
    data_sample = data
    tags_list = sorted(list(set(data_sample["tags"].values)))
    
    words_dict = sorted(list(set(data_sample["words"].values)))
    words_dict.append("OUT_OF_VOC")
    words_dict.append("Padded_Value")


    word2id = {w: i for i, w in enumerate(words_dict)}
    tag2id = {t: i for i, t in enumerate(tags_list)}
    
    
    sentence_token = sentence_tokenize(sentence)
    word_token = word_tokenize(sentence_token)
    stemmed_sentences = stem_words(word_token)
    X_samp = [[word2id.get(w, word2id['OUT_OF_VOC']) for w in s] for s in stemmed_sentences]
    X_Samp = pad_sequences(maxlen=50, sequences=X_samp, padding="post",value =word2id["Padded_Value"])
    loaded_model = load_model("first_app/pos_model_new.h5")
    p1 = loaded_model.predict(np.array(X_Samp)) # Predict on it
    pr = np.argmax(p1, axis=-1) # Map softmax back to a POS index
    tagged_sentences = []
    for sentence, pred in zip(stemmed_sentences, pr):
        tagged_sentence = []
        for w, t in zip(sentence, pred):
            tagged_sentence.append((w, pos_mapping.get(tags_list[t], 'Unclassifiable')))
        tagged_sentences.append(tagged_sentence)
    return tagged_sentences