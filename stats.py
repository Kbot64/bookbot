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