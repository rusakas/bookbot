import sys
from stats import get_word_count, get_character_count, chars_dict_to_sorted_list


def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    char_count = get_character_count(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(char_count)
    print_report(book_path, num_words, chars_sorted_list)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
main()