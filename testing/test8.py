a = [1,1,2,3,4,5,6,8,9,10]
b = [1,2,3,4,5]

a = range(1,10000000)

def median(lst):
    if len(lst) % 2 == 0:
        return (lst[int(len(lst)/2 - 1)] + lst[int(len(lst)/2)]) / 2
    else:
        return lst[int((len(lst) - 1) / 2)]

print(median(a))
print(median(b))

def mode(lst):
    m = 0
    for n in set(lst):
        c = lst.count(n)
        if c > abs(m):
            m = c
        if c == abs(m):
            m = -abs(m)
    return m if m > 0 else None

print(mode(a))

def mode_2(lst):
    dct = {}
    for n in lst:
        if n in dct.keys():
            dct[n] += 1
        else:
            dct[n] = 1
    n = 0
    for key, value in dct.items():
        if value > abs(n):
            n = value
            m = key
        elif value == abs(n):
            n = -value
    return m if n > 0 else None

print(mode_2(a))
        




