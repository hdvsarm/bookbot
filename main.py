from stats import word_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    contents=get_book_text("books/frankenstein.txt")
    num_words=word_count(contents)
    print(f"{num_words} words found in the document")


main()