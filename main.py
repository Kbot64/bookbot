import sys
from stats import book_word_count
from stats import num_of_each_char
from stats import make_sorted_dict_list

def get_book_contents(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(filepath):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count(get_book_contents(filepath))}")
    book_character_dictionary = num_of_each_char(get_book_contents(filepath))
    print("--------- Character Count -------")
    report_list = make_sorted_dict_list(book_character_dictionary)
    for dict in report_list:
        for key in dict:
            if key == "char" and dict["char"].isalpha():
                print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
        


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"Found {book_word_count(get_book_contents(sys.argv[1]))} total words")
    book_chars_dict = num_of_each_char(get_book_contents(sys.argv[1]))
    # print(book_chars_dict)
    report_list = make_sorted_dict_list(book_chars_dict)
    print_report(sys.argv[1])
main()