'https://www.codewars.com/kata/5f3afc40b24f090028233490/python'

def swap(s,n):
    bin_n = list(bin(n))[2:]
    print(bin_n)
    n_index = 0
    new_str = ''
    for char in s:
        if char.isalpha():
            if bin_n[n_index % len(bin_n)] == '1':
                if char.upper() == char:
                    new_str += char.lower()
                else:
                    new_str += char.upper()
            else:
                new_str += char
            n_index += 1
        else:
            new_str += char
    return new_str