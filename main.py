import sys
from stats import get_num_words, char_count, sort_list

if len(sys.argv) <2:
        print("Usage: python3 amin.py <path_to_book>")
        sys.exit(1)

path_to_file = sys.argv[1]

def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
        return file_contents

def main():
        total = get_num_words(get_book_text(path_to_file))
        counts =  char_count(get_book_text(path_to_file))
        sorted = sort_list(counts)
        print("")
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}")
        print("---------- Word Count ----------")
        print(f"Found {total} total words")
        print("--------- Character Count -------")
        for item in sorted:
                for char, count in item.items():
                        if char.isalpha():
                                print(f"{char}: {count}")
        print("============= END =============")
        print("")
main()
