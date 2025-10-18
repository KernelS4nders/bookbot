# imports the word count function from stats.py
from stats import word_count, char_count, sorted_list
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    # print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print(len(sys.argv))
        book = sys.argv[1]
        book_content = get_book_text(book)
        print("Analyzing book found at books/frankenstein.txt...")
        words = word_count(book_content)
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        all_char_counts = char_count(book_content)
        print("--------- Character Count -------")
        sorted_list(all_char_counts)
        print("============= END ===============")


main()
