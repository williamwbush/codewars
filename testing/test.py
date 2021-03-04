s = "BABBYBBYXAXXYBAYBXAYBXBYAYXBAXYBYBAAABYAXBAYYAYAAB"
others = list(s)

# XB Y YAXBYAXBB X AY B
# YAXBYBXB

# pairs = 0

# for i in range(len(ls)//2):
#     for i in range(len(ls)-1):
#         if ls[i] == 'A' and ls[i+1] == 'B' \
#             or (ls[i] == 'B' and ls[i+1] == 'A') \
#             or (ls[i] == 'X' and ls[i+1] == 'Y') \
#             or (ls[i] == 'Y' and ls[i+1] == 'X'):
#             pairs += 1
#             ls[i], ls[i+1] = ('C',)*2
#     while "C" in ls:
#         ls.remove('C')
# print(f'pairs = {pairs}')
# print(f'ls = {ls}')

# ls = ['B', 'B', 'Y', 'B', 'B', 'X', 'A', 'Y']
# ls = ['B', 'B', 'Y', 'B', 'B', 'X', 'A', 'Y', 'B', 'X', 'B', 'Y', 'Y', 'A', 'Y', 'A', 'Y', 'A', 'Y', 'A']
# pairs = 0
# for i in range(len(ls)//3):
#     for i in range(len(ls)-2):
#         print(f'index = {i}')
#         if ls[i] == 'A' and ls[i+2] == 'B' \
#             or (ls[i] == 'B' and ls[i+2] == 'A') \
#             or (ls[i] == 'X' and ls[i+2] == 'Y') \
#             or (ls[i] == 'Y' and ls[i+2] == 'X'):
#             pairs += 1
#             print(f'pairs = {pairs}')
#             ls[i], ls[i+1], ls[i+2] = ['C' for n in range(3)]
#     while "C" in ls:
#         ls.remove('C')
# print(f'pairs = {pairs}')
# print(f'ls = {ls}')


# def find_pairs(n):
#     pairs = 0
#     for i in range(len(ls)//2):
#         for i in range(len(ls) - n + 1):
#             if ls[i] == 'A' and ls[i+n-1] == 'B' \
#                 or (ls[i] == 'B' and ls[i+n-1] == 'A') \
#                 or (ls[i] == 'X' and ls[i+n-1] == 'Y') \
#                 or (ls[i] == 'Y' and ls[i+n-1] == 'X'):
#                 pairs += 1
#                 ls[i:i+n] = ['C' for i in range(n)]
#         while "C" in ls:
#             ls.remove('C')
#     print(f'pairs {n-1} apart = {pairs}')
#     print(f'new ls = {ls}')
#     return pairs


# all_pairs = 0
# for n in range(1, len(ls)):
#     if len(ls) > 1:
#         all_pairs += sum([find_pairs(n) for n in range(2,n+1)])
# print(all_pairs)





# for n in range(len(ls)):
#     while n <= len(find_pairs(n)[1]):
#         all_pairs += find_pairs(n)[0]
# all_pairs = [find_pairs(n) for n in range(len(ls))]

# while ('A' in ls and 'B' in ls) or ('X' in ls and 'Y' in ls):
#     distance += 1   
#     all_pairs += find_pairs(distance)
#     print(f'all pairs = {all_pairs}')
# print(all_pairs)



# other_pairs = 0
# chars = []

# for char in ls:
#     chars.append(char)
#     if 'X' in chars and 'Y' in chars \
#         or ('A' in chars and 'B' in chars):
#         other_pairs += 1
#         chars = []

# print(pairs)
# print(ls)
# print(other_pairs)
# print(pairs + other_pairs)

# other_pairs = max(min(ls.count('A'), ls.count('B')), min(ls.count('X'), ls.count('Y')))

# others = ['B', 'B', 'Y', 'B', 'B', 'X', 'A', 'Y', 'B', 'X', 'B', 'Y', 'Y', 'A', 'Y', 'A', 'Y', 'A', 'Y', 'A'

'A' 'X' 'A' 'Y' 'B' 'Y' 'B' 'X' 'A' 'X'

others = ['A', 'X', 'B', 'Y', 'A', 'X', 'B', 'Y', 'A', 'X', 'X', 'X', 'B']

# others = ['A', 'X', 'A', 'Y', 'B']


def twoPointers(others): 
    index = [0, len(others) - 1]
    pointer_pos = 0
    l_chars = []
    r_chars = []
    pairs = 0
    while index[0] <= index[1]:
        if pointer_pos % 2 == 0:
            l_chars.append(others[index[0]])
            print(f'l chars = {l_chars}')
        else:
            print(index[1])
            r_chars.append(others[index[1]])
            print(f'r_chars = {r_chars}')
        chars = l_chars + r_chars
        print(f'chars = {chars}')
        if 'X' in chars and 'Y' in chars \
            or ('A' in chars and 'B' in chars):
            pairs += 1
            print(f'pairs = {pairs}')
            if pointer_pos % 2 == 0:
                print('position 0')
                if l_chars[-1] == 'A':
                    if 'B' in l_chars:
                        index[1] += len(r_chars) - 1
                    else:
                        index[1] = len(others) - others[::-1].index('B') - 1
                    l_chars, r_chars = [], []
                elif l_chars[-1] == 'B':
                    if 'A' in l_chars:
                        index[1] += len(r_chars)
                    else:
                        index[1] = len(others) - others[::-1].index('A') - 1
                    l_chars, r_chars = [], []
                elif l_chars[-1] == 'X':
                    if 'Y' in l_chars:
                        index[1] += len(r_chars) - 1
                    else:
                        index[1] = len(others) - others[::-1].index('Y') - 1
                    l_chars, r_chars = [], []
                elif l_chars[-1] == 'Y':
                    print('l_char[-1] = Y')
                    if 'X' in l_chars:
                        index[1] += len(r_chars) - 1
                    else:
                        print(f'index[1] before change = {index[1]}')
                        index[1] = len(others) - others[::-1].index('X') - 1
                        print(f'index[1] after change = {index[1]}')
                    l_chars, r_chars = [], []
                index[0] += 1
                print(f'index[0] = {index[0]}')
            else:
                if r_chars[0] == 'A':
                    if 'B' in r_chars:
                        index[0] -= len(l_chars) + 1
                    else:
                        index[0] = others.index('B') + 1
                    l_chars, r_chars = [], []
                elif r_chars[0] == 'B':
                    if 'A' in r_chars:
                        index[0] -= len(l_chars) + 1
                    else:
                        index[0] = others.index('A') + 1
                    l_chars, r_chars = [], []
                elif r_chars[0] == 'X':
                    if 'Y' in r_chars:
                        index[0] -= len(l_chars) + 1
                    else:
                        index[0] = others.index('Y') + 1
                    l_chars, r_chars = [], []
                elif r_chars[0] == 'Y':
                    if 'X' in r_chars:
                        index[0] -= len(l_chars) + 1
                    else:
                        index[0] = others.index('X') + 1
                    l_chars, r_chars = [], []
                index[1] -= 1
        else:
            if pointer_pos % 2 == 0:
                index[0] += 1
            else:
                index[1] -= 1
        pointer_pos += 1
        print(f'pointer position = {pointer_pos % 2}')
    print(pairs)
   
twoPointers(others)