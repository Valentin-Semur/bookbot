def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    print(f"The are {number_of_words} words in the book {book_path}")

def get_book_text(book_path):
    with open(book_path, 'r') as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

main()