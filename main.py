from stats import word_count, char_count, dict_sort
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    try:
        book_path=sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents=get_book_text(book_path)
    num_words=word_count(contents)
    char_dict=char_count(contents)
    sorted_chars=dict_sort(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")


    

main()