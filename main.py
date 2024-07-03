#print("hello world")
def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path) 
    num_words = get_num_words(text)
    print(f"{num_words} words found in this document.")
    letter_count = {}
    lowered_text = text.lower()
    just_letters = []
    for char in lowered_text:
        just_letters.append(char)
    
#def letter_counter(just_letters):
    for letter in just_letters:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else: 
                letter_count[letter] = 1
    print(letter_count)







def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


main()
