# https://www.codewars.com/kata/5592e3bd57b64d00f3000047

def find_nb(m):
    p = 1
    while m > 0:
        m -= p**3
        if m == 0:
            return p
        p += 1
    return -1

print(find_nb(100))