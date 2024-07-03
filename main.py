#print("hello world")
def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path) 
    num_words = get_num_words(text)
    letter_dict = alpha_char_dict(text)
    sorted_dict = sort_reverse(letter_dict)
    list_of_dict = dict_to_list(sorted_dict)
    print(f"the {list_of_dict[0].keys()} character was found {list_of_dict[0].values} times")




def sort_reverse(letter_dict):
    sort = (dict(sorted(letter_dict.items(), key = lambda x:x[1], reverse = True)))
    return sort

def dict_to_list(letter_dict):
    dict_list = []
    for char, num in letter_dict.items():
        dict_list.append({char: num})
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




def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


main()
