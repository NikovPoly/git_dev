#!/usr/bin/env python3
"""
palindrome_checker.py
This program tests to see if a string is a palindrome and returns True of False accordingly
"""

__author__ = "Niko Vidalaks"
__version__ = "January 17 2023"

from atds import Deque

def set_strict_mode():
    s = input('Do want strict mode? 1->yes 2-> no:')
    if int(s) == 1:
        return True
    else:
        return False
def clean(phrase):
    return_phrase = ''
    bad_list=[',',' ', '?','.', "'",'"',"!"]
    for letter in phrase:
        if letter not in bad_list:
            return_phrase +=(letter.lower())
    return return_phrase
def is_palindrome(sen):
    sentence = sen
    if set_strict_mode() == False:
        sentence =clean(sentence)
    front = Deque()
    back = Deque()
    for letter in sentence:
        front.add_front(letter)
        back.add_rear(letter)
    if front.to_string() == back.to_string():
        return True
    else:
        return False
    




def main():
    print(is_palindrome("Madam in Eden, I'm Adam!"))
    print(is_palindrome("Madam in Eden, I'm Adam!"))
    print(is_palindrome("racecar a racecar"))

if __name__ == "__main__":
    #what does the line above do
    main()