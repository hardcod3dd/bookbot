def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    letters = num_letters(file_contents)
    words = num_words(file_contents)
    letters_sorted = sort_on(letters)

    print("=====Report for the book.=====")
    print(f"There are {words} words.")
    print(f"Most used letters are :")
    for i in letters_sorted:
        if not i.isalpha():
            continue
        print(f"The letter {i} appears {letters_sorted[i]} times.")
    print("=====End of report=====")

def num_words(text):
    words = text.split()
    return len(words)

def num_letters(text):
    result = {}
    lowered = text.lower()
    for i in lowered:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

def sort_on(words):
    return dict(sorted(words.items(), key=lambda x: x[1],reverse=True))


main()