def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    letter_count, number_count = count_characters(text)
    sorted_letters = sort_letters(letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

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


def sort_letters(letters):
    sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)

    return sorted_letters

main()