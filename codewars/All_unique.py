'''
codewars.All_unique의 Docstring

Write a program to determine if a string contains only unique characters. Return true if it does and false otherwise.

The string may contain any of the 128 ASCII characters. Characters are case-sensitive, e.g. 'a' and 'A' are considered different characters.
'''

def has_unique_chars(string):  
    setString = set(string)
    
    len_string, len_setString = len(string), len(setString)
    
    if len_string == len_setString:
        return True
    
    else:
        return False
    
    pass
