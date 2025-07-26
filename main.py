import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def stats(filepath):
    book_text = get_book_text(filepath)

    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_characters = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_characters:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    stats(book_path)
