from stats import book_word_count
from stats import num_of_each_char

def get_book_contents(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    # print(get_book_contents("books/frankenstein.txt"))
    print(f"Found {book_word_count(get_book_contents("books/frankenstein.txt"))} total words")
    book_chars_dict = num_of_each_char(get_book_contents("books/frankenstein.txt"))
    print(book_chars_dict)
main()