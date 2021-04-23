'https://www.codewars.com/kata/5d98b6b38b0f6c001a461198/python'

strng1 = '55337700'
strng2 = '001101001101011101110011110011111010'

def code(strng):
    return "".join('0' * (len(bin(int(d))) - 3) + '1' + str(bin(int(d)))[2:] for d in list(strng))
        
def decode(strng):
    decoded = ""
    while strng:
        bin_length = strng.index('1') + 1
        decoded += str(int(strng[bin_length: bin_length * 2], 2))
        strng = strng[bin_length * 2:]
    return decoded

print(code(strng1))
print(decode(strng2))