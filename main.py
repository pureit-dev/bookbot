def main():
    book_path = "books/frankenstien.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    count_letters(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return list(dict.values())[0]

def count_letters(text):
    text = text.lower()
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            if char.isalpha():
                result[char] = 1
    char_list = [{key: value} for key, value in result.items()]
    char_list.sort(key=sort_on, reverse=True)
    for i in char_list:
        for key, value in i.items():
            print(f"The '{key}' character was found {value} times")
main()