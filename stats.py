import sys
def get_words(text):
    words = text.split()
    return len(words)

def get_book_text():
    arguments = sys.argv
    book = arguments[1]
    with open(book) as f:
        return f.read()
    
def get_characters():
    characters = {}
    text = get_book_text()
    
    for texx in text:
        tex = texx.lower()
        if tex.isalpha() == True:
            characters[tex] = characters.get(tex,0) +1
        
    return characters

def get_sorted_characters():
    characters = get_characters()

    sort_characters = sorted(characters.items(), key=lambda x:x[1],reverse=True)
    sorted_dict = dict(sort_characters)
    
    for dic in sorted_dict:
        val = sorted_dict[dic]
        print(f"{dic}: {val}")
    return 0


    

