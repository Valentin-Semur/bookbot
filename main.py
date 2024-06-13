def main():
    with open("books/frankestein.txt", 'r') as file:
        text = file.read()
    print(text)

main()