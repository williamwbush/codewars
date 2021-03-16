# https://www.codewars.com/kata/604f8591bf2f020007e5d23d

# Write a function that receives a non-negative integer n ( n >= 0 ) and returns the next higher multiple 
# of five of that number, obtained by concatenating the shortest possible binary string to the end of 
# this number's binary representation.

def next_multiple_of_five(n):
    b = str(bin(n))[2:]
    i = 0
    
    while True:
        next = b + str(bin(i))[2:][::-1]
        if int(next, 2) % 5 == 0 and int(next, 2):
            return int(next, 2)
        i += 1