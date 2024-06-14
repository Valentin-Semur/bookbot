def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    letter_count, number_count = count_characters(text)

    print(f"The are {number_of_words} words in the book {book_path}")
    print(f"The letter count is: {letter_count}")
    print(f"The number count is: {number_count}")

def get_book_text(book_path):
    with open(book_path, 'r') as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    letters = {a: 0 for a in "abcdefghijklmnopqrstuvwxyz"}
    numbers = {i: 0 for i in "0123456789"}

    for char in text:
        if char.isalpha():
            letters[char.lower()] += 1
        elif char.isnumeric():
            numbers[char] += 1
    
    return letters, numbers


main()