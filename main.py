def main():
    path = 'books/frankenstein.txt'
    text = get_text(path)
    words = count_words(text)
    letters = count_letters(text)
    print(f"--- Begin report of {path}")
    print(f"There are {words} words in this document")
    print()
    for letter in letters:
        print(f"The {letter} character was found {letters[letter]} times")
    print("--- End report ---")

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for char in text.lower():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

main()

