
from ntpath import join


input = input("Type text to convert into acronym: ")


def acronym(text):
    first_letters=[]
    words = text.split()
    
    for word in words:
        if word.isalpha() & (word != 'and')==1:
            first_letters.append((word[0]).upper())
    
    print(''.join(first_letters))

acronym(input)