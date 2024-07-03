#print("hello world")
def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path) 
    num_words = get_num_words(text)
    print(f"{num_words} words found in this document.")
    letter_dict = {}
    lowered_text = text.lower()
    just_letters = []
    for char in lowered_text:
        just_letters.append(char)
    



#def letters_dict():
    

    #for i in lowered_text:
        #letter_dict.update({i: += 1})



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


main()
