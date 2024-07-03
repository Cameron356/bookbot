#print("hello world")
def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path) 
    num_words = get_num_words(text)
    letter_dict = alpha_char_dict(text)
    list_of_dict = dict_to_list(letter_dict)
    print(list_of_dict)


def dict_to_list(letter_dict):
    dict_list = []
    for char, num in letter_dict.items():
        dict_list.append({char: num})
    dict_list.sort()
    return dict_list


def alpha_char_dict(text):    
    char = {}
    for letter in text:
        lowered = letter.lower()
        if letter.isalpha():
            if lowered in char:
                char[lowered] += 1
            else:
                char[lowered] = 1
    return char

##def letter_counter(just_letters):
#    for letter in just_letters:
#        if letter.isalpha():
#            if letter in letter_count:
#                letter_count[letter] += 1
#            else: 
#                letter_count[letter] = 1
#    print(letter_count)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


main()
