def main():
    path = 'books/frankenstein.txt'
    text = get_text(path)
    words = count_words(text)
    chars = count_chars(text)
    chars_sorted = sort_chars(chars)
    print(f"--- Begin report of {path}")
    print(f"There are {words} words in this document")
    print()
    for char in chars_sorted:
        print(f"The \"{char["char"]}\" character was found {char["num"]} times")
    print("--- End report ---")

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_chars(chars):
    chars_list = []
    for char in chars:
        if char.isalpha():
            chars_list.append({"char": char, "num": chars[char]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

main()

