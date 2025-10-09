import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_dicts

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.ext(1)

def get_book_text():
    with open(sys.argv[1]) as f:
        return f.read()

def main():
    num_words = get_num_words(get_book_text())
    num_chars = get_num_characters(get_book_text())
    sorted_chars = sort_dicts(num_chars)
    print("============ BOOKBOT ============\nAnalyzing book found at path...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print(f"--------- Character Count -------\n")
    for i in sorted_chars:
        print(f"{i["char"]}: {i["num"]}\n")
    print("============= END ===============")
    print(sys.argv)
main()
