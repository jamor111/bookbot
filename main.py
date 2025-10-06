#!/usr/bin/env python3
import sys
from stats import get_words, get_book_text, get_characters, get_sorted_characters


def main():

    arguments = sys.argv
    length = len(arguments)
    if length <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    


    text = get_book_text()
    result = get_words(text)
    book = arguments[1]
    bookname = book.split("/")
    
    

    print("===================--- BOOKBOT ---===================")
    print(f"Book name: {bookname[1][:-4]}")
    print("=====================================================")
    print(f"Found {result} total words")

    get_sorted_characters()
    

    
    

    

main()
