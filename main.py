def get_book_text(bookpath: str) -> str:
    with open(bookpath) as f:
        return f.read()


def get_word_num(string: str) -> int:
    return len(string.split())


def get_count_characters(string: str) -> dict:
    chars = {}
    for char in string.lower():
        # Nicer would be: if char in chars
        if chars.get(char) is not None:
            chars[char] = chars[char] + 1
        else:
            chars[char] = 1
    return chars


def order_chars(chars: dict) -> list:
    listed = [{"char": k, "count": v} for k, v in chars.items()]
    listed.sort(reverse=True, key=word_dict_sorter)
    return listed


def word_dict_sorter(dict):
    return dict["count"]


def nice_printer(path: str, wordcount: int, chars: dict):
    print(f"--- Begin report of {path} ---")
    print(f"{wordcount} words found in the document")
    sorted_chars = order_chars(chars)
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"The '{char["char"]}' character was found {char["count"]} times")
    print("--- End report ---")


def main():
    path = "books/frankenstein.txt"
    book = get_book_text(path)
    # print(get_word_num(book))
    chars = get_count_characters(book)
    wordcount = get_word_num(book)
    nice_printer(path, wordcount, chars)


if __name__ == "__main__":
    main()
