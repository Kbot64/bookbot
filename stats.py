def book_word_count(book_string): 
    return len(book_string.split())

def num_of_each_char(book_string):
    char_set = set()
    book_words = book_string.split()
    char_dict = dict()
    for w in book_words:
        for l in w:
            if l.lower() in char_set and l.lower() in char_dict:
                char_dict[l.lower()] += 1
            else:
                char_set.add(l.lower())
                char_dict[l.lower()] = 1
        
    return char_dict

def get_num(dictionary):
    return dictionary["num"]



def make_sorted_dict_list(dictionary):
    list_of_dictionaries = []
    for k in dictionary:
        temp_dictionary = {}
        temp_dictionary["char"] = k
        temp_dictionary["num"] = dictionary[k]
        list_of_dictionaries.append(temp_dictionary)
        list_of_dictionaries.sort(reverse=True, key=get_num)
    return list_of_dictionaries

