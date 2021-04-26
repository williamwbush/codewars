'https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/python'

def clean_string(s):
    new_s = ''
    for c in list(s):
        if c == '#':
            new_s = new_s[:-1]
        else:
            new_s += c
    return new_s

print(clean_string("abc#d##c"))