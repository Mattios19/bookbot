import sys
from stats import count_words, count_characters, sort_characters_by_count

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        return content

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    book_text = get_book_text(file_path)
    #print(book_text)  # Print the contents or error message

    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_count = count_characters(book_text)
    sorted_char_list = sort_characters_by_count(char_count)

    for entry in sorted_char_list:
        print(f"{entry['char']}: {entry['count']}")

if __name__ == "__main__":
    main()

