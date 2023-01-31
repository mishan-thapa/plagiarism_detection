import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn



eng_punctuations = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

stopwords_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll",
             "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's",
             'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 
             'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 
             'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
             'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 
             'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 
             'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off',
             'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why',
             'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 
             'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
             "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't",
             'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 
             'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn',
             "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't",
             'won', "won't", 'wouldn', "wouldn't"]


def preprocessing(text):
# changing punctuation into white space
    for punctuation in eng_punctuations:
        text = text.replace(punctuation, ' ')
        
    #now tokenizing   
    token = text.strip().split()

    #removing the stop words
    new_tokens = list() #new_tokens hold the list of words after removing stopwords
    for token in token:
        if token not in stopwords_list:
            new_tokens.append(token)
    
    return new_tokens



def calculate_wordsimilarity(source_text,suspicious_text):
    

    cleaned_tokenized_suspicious_text = preprocessing(suspicious_text)
    cleaned_tokenized_source_text = preprocessing(source_text)
    #print(cleaned_tokenized_suspicious_text)
    #print(cleaned_tokenized_source_text)
    words_from_suspicious=nltk.pos_tag(cleaned_tokenized_suspicious_text)
    words_from_source=nltk.pos_tag(cleaned_tokenized_source_text)
    #print(words_from_suspicious)
    #print(words_from_source)
    
    
    lemmatizer = WordNetLemmatizer()

    def nltk_tag_to_wordnet_tag(nltk_tag):
        if nltk_tag.startswith('J'):
            return "a"
        elif nltk_tag.startswith('V'):
            return "v"
        elif nltk_tag.startswith('N'):
            return "n"
        elif nltk_tag.startswith('R'):
            return "r"
        else:         
            return "other"  
    def lemmatizing_with_wntag(words):
        lematized_words = list()
        for word, pos in words:
            temp = tuple()
            wn_tag = nltk_tag_to_wordnet_tag(pos)
            if wn_tag != "other":
                lemmatized_word = lemmatizer.lemmatize(word,wn_tag)
            else:
                lemmatized_word = lemmatizer.lemmatize(word)
            temp = (lemmatized_word,wn_tag)
            lematized_words.append(temp)
        return lematized_words
    words_suspicious_with_wntag = lemmatizing_with_wntag(words_from_suspicious)
    words_source_with_wntag = lemmatizing_with_wntag(words_from_source)
    #print(words_suspicious_with_wntag)
    #print(words_source_with_wntag)
    #len(words_suspicious_with_wntag)
    def finding_synsets(token):
        synsets = dict()
        for word , pos in token:
            if pos.startswith('j'):
                tb=wn.synsets(word,wn.ADJ)
            elif pos.startswith('v'):
                tb=wn.synsets(word,wn.VERB)
            elif pos.startswith('n'):
                tb=wn.synsets(word,wn.NOUN)
            elif pos.startswith('r'):
                tb=wn.synsets(word,wn.ADV)
            else:
                tb=wn.synsets(word)

            synsets[word]=tb
        return synsets
    synsets_of_suspicious = finding_synsets(words_suspicious_with_wntag)
    #print(synsets_of_suspicious)
    def finding_similar_word(synsets):
        similar_word = dict()
        for word in synsets:
            synset_word = synsets[word]
            temp = list()

            for syn in synset_word:
                for l in syn.lemmas():
                    temp.append(l.name().lower())

            temp = list(set(temp))
            similar_word[word]=temp
        return similar_word
    similar_words_suspicious = finding_similar_word(synsets_of_suspicious)
    #print(similar_words_suspicious)
    #len(similar_words_suspicious)
    def checking_similar_with_source(token_from_source):
        modified_source_token =list()
        for word , pos in words_source_with_wntag:
            temp =tuple()
            #print(word,pos)
            for key in similar_words_suspicious:
                #print(key)
                if word in similar_words_suspicious[key]:
                    temp=(key,pos)
                    #break
            #print(len(temp))
            if len(temp) != 0 :
                modified_source_token.append(temp)
            else:
                temp = (word,pos)
                modified_source_token.append(temp)
            #print(temp)
        return modified_source_token
    new_words_source_with_wntag = checking_similar_with_source(words_source_with_wntag)
    #print(new_words_source_with_wntag)
    #len(new_words_source_with_wntag)
    def jaccard_similarity(list1, list2):
        s1 = set(list1)
        s2 = set(list2)
        return float(len(s1.intersection(s2)) / len(s1.union(s2)))
    list1 = words_suspicious_with_wntag
    list2 = new_words_source_with_wntag
    similarity=jaccard_similarity(list1, list2)
    return similarity

