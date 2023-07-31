import json
from pygtrie import Trie

    # Create a Trie data structure
trie = Trie()

def remove_spaces_from_list_elements(input_list):
    return [word.replace(' ', '') for word in input_list if word]

def search_synonyms(word):
    if word in trie:
        return trie.get(word, None)
    

def get_all_synonyms(search_word):
    # Load the JSON file
    with open('first_app/output.json') as file:
        data = json.load(file)
    # Iterate over all data elements
    for entry in data:
        word = entry['word']
        synonyms = entry['synonyms']
        # Insert the word and its qualifying senses into the Trie
        trie[word] = synonyms
        
    synonyms = search_synonyms(search_word)
    all_synonyms = []
    all_synonyms.extend(synonyms)

    if synonyms is None:
        return []
    else:
        synonyms = remove_spaces_from_list_elements(synonyms)
        for word in synonyms:
            if word:
                synonyms_list = trie.get(word, None)
                # Print the word and its synonyms
                if synonyms_list is not None:
                    for sense in synonyms_list:
                        all_synonyms.append(sense)

        all_synonyms = remove_spaces_from_list_elements(all_synonyms)
        all_synonyms = list(set(all_synonyms))

    return all_synonyms