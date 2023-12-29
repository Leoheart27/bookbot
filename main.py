def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    letters_sorted_list = chars_dict_to_sorted_list(num_letters)
    print("--Begin report of books/frankenstein--")
    print(f"{num_words} letras foram encontradas no documento.")

    for item in letters_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was fount {item['num']} times")

    print("--The End--")

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_num_letters(text):
    letters = {}
    for t in text:
        if t.lower() in letters:
            letters[t.lower()] += 1
        else:
            letters[t.lower()] = 1
    return letters

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()