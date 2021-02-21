from math import factorial as f
from functools import reduce

# question
# [einoqstu]
# pos = 4*f(7) + 6*f(6) + 0*f(5) + 3*f(4) + 3*f(3) + 0*f(2) + 1*f(1) + 1
# print(pos)

# 4! / 4 + 4! / 2
# 3 * 4! / 4
# BEKKOO
# BEKOKO
# BEKOOK
# BEOKKO
# BEOKOK
# BEOOKK
# BKEKOO
# BKEOKO
# BKEOOK
# BKKEOO
# BKKOEO
# BKKOOE
# BKOEKO
# BKOEOK
# BKOKEO
# BKOKOE
# BKOOEK
# BKOOKE
# BOEKKO
# BOEKOK
# BOEOKK
# BOKEKO
# BOKEOK
# BOKKEO
# BOKKOE
# BOKOEK
# BOKOKE
# BOOEKK
# BOOKEK
# BOOKKE



word = "IMMUNOELECTROPHORETICALLY"

def unique(word):
    return sorted(list(set(word)))

def non_unique_comb(word):
    if _print == True:
        print("finding non_unique_comb")
    non_unique_factorials = [f(word.count(unique(word)[i])) for i in range(len(unique(word))) if word.count(unique(word)[i]) > 1]
    
    if _print == True:
        print(f"word: {word}")
        print(f"non_unique_factorials: {non_unique_factorials}")
    return reduce((lambda a, b: a * b), non_unique_factorials, 1) if non_unique_factorials else 1

def non_unique_combs(word):
    if _print == True:
        print("finding non_unique_combs")
    output = list(non_unique_comb(word[:word.index(unique(word)[i])] + word[word.index(unique(word)[i])+1:]) for i in range(0,unique(word).index(word[0])))
    if _print == True:
        print(f"word: {word}")
        print(f"non_unique_combs: {output if output != 0 else 1}")
    return output if sum(output) != 0 else [1]

def combs(word, i):
    print(f"combs: {sum( map(  lambda comb: int(int(f(len(word) - i - 1)) / comb),  non_unique_combs(word[i:]) )  )}")
    return sum( map(  lambda comb: f(len(word) - i - 1) / comb,  non_unique_combs(word[i:]) )  )


_print = False    
print(sum(combs(word,i) for i in range(len(word)-1) if word[i] != unique(word[i:])[0]) + 1)


# SECOND VERSION FOR CODEWARS

# def unique(word):
#     return sorted(list(set(word)))

# def non_unique_comb(word):
#     non_unique_factorials = [f(word.count(unique(word)[i])) for i in range(len(unique(word))) if word.count(unique(word)[i]) > 1]
#     return reduce((lambda a, b: a * b), non_unique_factorials, 1) if non_unique_factorials else 1

# def non_unique_combs(word):
#     output = list(non_unique_comb(word[:word.index(unique(word)[i])] + word[word.index(unique(word)[i])+1:]) for i in range(0,unique(word).index(word[0])))
#     return output if sum(output) != 0 else [1]

# def combs(word, i):
#     return sum( map(  lambda comb: f(len(word) - i - 1) / comb,  non_unique_combs(word[i:]) )  )
 
# return sum(combs(word,i) for i in range(len(word)-1) if word[i] != unique(word[i:])[0]) + 1





# FIRST SOLUTION THAT WORKED FOR "QUESTION"

# def listPosition(word):
#     from math import factorial as f
#     from functools import reduce
    
#     def unique(word):
#         return sorted(list(set(word)))

#     def non_unique_comb(word):
#         non_unique_factorials = [f(word.count(unique(word)[i])) for i in range(len(unique(word))) if word.count(unique(word)[i]) > 1]
#         return reduce((lambda a, b: a * b), non_unique_factorials, 1) if non_unique_factorials else 0
    
#     def non_unique_combs(word):
#         output = sum(non_unique_comb(word[:word.index(unique(word)[i])] + word[word.index(unique(word)[i])+1:]) for i in range(0,unique(word).index(word[0])))
#         return output if output != 0 else 1
        
#     return sum((unique(word[i:]).index(word[i]) * f(len(word) - i - 1)) / (non_unique_combs(word[i:])) for i in range(len(word)-1)) + 1



# 628347629070120976384
# 628347629070120960000

# finding non_unique_comb
# word: IMMUNOELECTROPHORETICLLY
# non_unique_factorials: [2, 6, 2, 6, 2, 6, 2, 2]
# finding non_unique_comb
# word: IMMUNOELETROPHORETICALLY
# non_unique_factorials: [6, 2, 6, 2, 6, 2, 2]
# finding non_unique_comb
# word: IMMUNOLECTROPHORETICALLY
# non_unique_factorials: [2, 2, 2, 6, 2, 6, 2, 2]
# finding non_unique_comb
# word: IMMUNOELECTROPORETICALLY
# non_unique_factorials: [2, 6, 2, 6, 2, 6, 2, 2]
# word: IMMUNOELECTROPHORETICALLY
# non_unique_combs: [6912, 3456, 2304, 6912]
# combs: 628347629070120976384


# PYTHON FAILING TO DIVIDE A LARGE NUMBER CORRECTLY
# >>> int(269291841030051856384/3)
# 89763947010017280000
# >>> 89763947010017280000 * 3
# 269291841030051840000


